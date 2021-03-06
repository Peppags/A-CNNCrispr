# -*- coding:utf-8 -*-

import os
os.environ["CUDA_VISIBLE_DEVICES"] = "0"

import keras
from keras.initializers import RandomUniform
from keras.layers import multiply
from keras.layers.core import Reshape, Permute
from keras.layers import BatchNormalization, Activation
from keras.layers.core import Dense, Dropout, Lambda, Flatten
from keras.layers.convolutional import Conv1D
from keras.layers.embeddings import Embedding
from keras.models import *
import numpy as np
from sklearn.model_selection import train_test_split


def attention(x, g, TIME_STEPS):
    """
    inputs.shape = (batch_size, time_steps, input_dim)
    """
    input_dim = int(x.shape[2])
    x1 = K.permute_dimensions(x, (0, 2, 1))
    g1 = K.permute_dimensions(g, (0, 2, 1))

    x2 = Reshape((input_dim, TIME_STEPS))(x1)
    g2 = Reshape((input_dim, TIME_STEPS))(g1)

    x3 = Dense(TIME_STEPS, kernel_initializer=RandomUniform(seed=2020))(x2)
    g3 = Dense(TIME_STEPS, kernel_initializer=RandomUniform(seed=2020))(g2)
    x4 = keras.layers.add([x3, g3])
    a = Dense(TIME_STEPS, activation='softmax', use_bias=False)(x4)
    a_probs = Permute((2, 1))(a)
    output_attention_mul = multiply([x, a_probs])
    return output_attention_mul


def loadData(data_file):
    data_list, label, negative, positive = [], [], [], []
    with open(data_file) as f:
        for line in f:
            ll = [i for i in line.strip().split(',')]
            label_item = np.float(ll[2])
            data_item = [int(i) for i in ll[3:]]
            if label_item == 0.0:
                negative.append(ll)
            else:
                positive.append(ll)
            data_list.append(data_item)
            label.append(label_item)
    return negative, positive, label


VOCAB_SIZE = 16
EMBED_SIZE = 90
BATCH_SIZE = 256
MAXLEN = 23

negative, positive, label = loadData('data/test_off-target.txt')

positive, negative = np.array(positive), np.array(negative)

train_positive, test_positive = train_test_split(positive, test_size=0.2, random_state=42)
train_negative, test_negative = train_test_split(negative, test_size=0.2, random_state=42)

xtest = np.vstack((test_negative, test_positive))
xtest = np.array(xtest)


def main():
    input = Input(shape=(23,))
    embedded = Embedding(VOCAB_SIZE, EMBED_SIZE, input_length=MAXLEN)(input)

    conv1 = Conv1D(20, 5, name="conv1")(embedded)
    ac1 = Activation('relu')(conv1)
    B1 = BatchNormalization()(ac1)

    conv2 = Conv1D(40, 5, name="conv2")(B1)
    ac2 = Activation('relu')(conv2)
    B2 = BatchNormalization()(ac2)

    conv3 = Conv1D(80, 5, name="conv3")(B2)
    ac3 = Activation('relu')(conv3)
    B3 = BatchNormalization()(ac3)

    conv11 = Conv1D(80, 9, name="conv11")(B1)
    x = Lambda(lambda x: attention(x[0], x[1], 11))([conv11, B3])

    flat = Flatten()(x)
    dense1 = Dense(40, name="dense1")(flat)
    ac4 = Activation('relu')(dense1)
    drop1 = Dropout(0.2)(ac4)

    dense2 = Dense(20, name="dense2")(drop1)
    ac5 = Activation('relu')(dense2)
    drop2 = Dropout(0.2)(ac5)

    dense3 = Dense(2, name="dense3")(drop2)
    output = Activation('softmax')(dense3)

    model = Model(inputs=[input], outputs=[output])

    print("Loading weights for the models")
    model.load_weights('weights/CRISPR-OFFT.h5')

    print("Predicting on test data")
    y_pred = model.predict(xtest[:, 3:])
    print(y_pred)


if __name__ == '__main__':
   main()
