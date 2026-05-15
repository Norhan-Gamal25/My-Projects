# ASL Classification CNN

## Overview
This repository contains a Convolutional Neural Network (CNN) built with TensorFlow and Keras to classify American Sign Language (ASL) alphabet images. The primary objective is to provide an efficient, highly accurate computer vision model capable of recognizing static ASL gestures, prioritizing robust evaluation and practical application.

## Dataset & Preprocessing
The model trains on a standardized ASL alphabet dataset. The data pipeline is structured for optimal generalization:
* **Resolution**: Images are resized to 64x64 pixels (`IMG_SIZE = 64`) to balance feature retention with computational efficiency.
* **Data Augmentation**: Applied rotation, zooming, width/height shifting, and horizontal flipping to the training set. This is a strict requirement to mitigate overfitting and simulate real-world input variance.
* **Normalization**: Pixel values are rescaled to `[0, 1]`.

## Model Architecture
The network is designed for precise feature extraction without unnecessary computational overhead. The architecture consists of:
1. **Convolutional Blocks**: Three `Conv2D` layers (32, 64, and 128 filters) utilizing ReLU activation, each immediately followed by `MaxPooling2D` to downsample spatial dimensions.
2. **Regularization**: `BatchNormalization` and `Dropout` layers are integrated strategically to stabilize the learning process and penalize over-reliance on specific neural pathways.
3. **Classification Head**: The extracted features are flattened and passed through a 256-unit `Dense` layer, terminating in a softmax output layer mapped to the ASL classes.

## Training Configuration
* **Batch Size**: 32
* **Epochs**: 20 
* **Optimizer**: Adam
* **Loss Function**: Categorical Crossentropy
* **Callbacks Implemented**: 
  * `EarlyStopping`: Monitors validation loss to halt training when no improvement is observed, ensuring efficient use of compute time.
  * `ReduceLROnPlateau`: Dynamically scales down the learning rate when validation accuracy plateaus to guarantee precise convergence.

## Results
The model was evaluated against an unseen test set to ensure strict, unbiased metrics. 
* **Final Test Accuracy**: 98.15%
* **Final Test Loss**: 0.0646

Classification reports confirm F1-scores consistently between 0.94 and 1.00 across the alphabet classes, indicating a highly reliable model with minimal class bias.

## Execution Requirements
To replicate these results, ensure the following core dependencies are installed in your environment:

```bash
pip install numpy pandas matplotlib seaborn scikit-learn tensorflow