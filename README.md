# A-CNNCrispr

## Overview
A-CNNCrispr is an attention-based convolution neural networks (CNN) framework to accurately predict the CRISPR/Cas9 sgRNA on-target activity. By integrating the convolutional neural network with attention mechanism, A-CNNCrispr is able to extract interpretable patterns that can provide useful and detailed insights into the sgRNA cleavage efficacy.

## Pre-requisite:  
* **Ubuntu 16.04**
* **Anaconda 3-5.2.0**
* **Python packages:**   
  [numpy](https://numpy.org/) 1.16.4  
  [pandas](https://pandas.pydata.org/) 0.23.0  
  [scikit-learn](https://scikit-learn.org/stable/) 0.19.1  
  [scipy](https://www.scipy.org/) 1.1.0  
 * **[Keras](https://keras.io/) 2.1.0**    
 * **Tensorflow and dependencies:**   
  [Tensorflow](https://tensorflow.google.cn/) 1.4.0    
  CUDA 8.0 (for GPU use)    
  cuDNN 6.0 (for GPU use)    
  
## Installation guide
#### **Operation system**  
Ubuntu 16.04 download from https://www.ubuntu.com/download/desktop  
#### **Python and packages**  
Download Anaconda 3-5.2.0 tarball on https://www.anaconda.com/distribution/#download-section  
#### **Tensorflow installation:**  
pip install tensorflow-gpu==1.4.0 (for GPU use)  
pip install tensorflow==1.4.0 (for CPU use)  
#### **CUDA toolkit 8.0 (for GPU use)**     
Download CUDA tarball on https://developer.nvidia.com/compute/cuda/8.0/Prod2/local_installers/cuda_8.0.61_375.26_linux-run  
#### **cuDNN 6.1.10 (for GPU use)**      
Download cuDNN tarball on https://developer.nvidia.com/cudnn  
 
## Content
* **./data/test_data.csv:** The testing examples with sgRNA sequence and corresponding biological features and label indicating the on-target cleavage efficacy  
* **./weights/A_CNNCrispr_weights.h5:** The well-trained weights for our A-CNNCrispr model
* **./weights/A-CNNCrispr_Bio_weights.h5:** The well-trained weights for our A-CNNCrispr+Bio model
* **./A-CNNCrispr.py:** The python code of A-CNNCrispr model, it can be ran to reproduce our results
* **./A-CNNCrispr_Bio.py:** The python code of A-CNNCrispr+Bio model, it can be ran to reproduce our results 

## Usage
#### **python A-CNNCrispr.py** 
#### **python A-CNNCrispr_Bio.py**
**Note:**  
* The input testing files should include sgRNA sequence with length of 23 bp, two corresponding biological features and label in each sgRNA sequence.    
* The test_data.csv can be replaced or modified to include sgRNA sequence and two biological features of interest  



