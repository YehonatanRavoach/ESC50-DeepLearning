# ESC-50 Environmental Sound Classification 🎵

This project implements deep learning classification on the [ESC-50 dataset](https://github.com/karolpiczak/ESC-50) for environmental sound recognition, leveraging a customized **ResNet-18-based CNN** architecture.

We focus on building a full, scalable pipeline — from EDA and data preprocessing to model training, evaluation, and performance analysis.

---

## 📁 Project Structure
project-root/   
│── notebooks/   
│ ├── 01_EDA.ipynb              # Exploratory Data Analysis  
│ ├── 02_Preprocessing.ipynb    # Data preparation, augmentation, feature engineering   
│ ├── 03_Modeling.ipynb         # CNN modeling, training, evaluation    
│ │── config.py                 # Centralized configuration file    
│── download_data.py            # Script to download the ESC-50 dataset     
│── README.md                   # Project documentation    
│── .gitignore  


---

## 🚀 Project Overview

Environmental Sound Classification is a complex task due to high variability in natural and human-made sounds.  
Our goal is to build a **high-accuracy deep learning model** for classifying 50 sound classes grouped into 5 broad categories.

We implement a **ResNet-18** model adapted for single-channel spectrograms and optimize it through careful preprocessing and data augmentation.

---

## 🛠️ Key Components

### 1. Exploratory Data Analysis (EDA)

- Analyzed dataset distribution: 50 balanced.
- Verified audio file integrity and durations (all ~5 seconds).
- Visualized waveforms and mel-spectrograms for understanding sound patterns.
- Extracted features such as **energy**, **tone** (spectral centroid), and grouped sounds accordingly.

### 2. Preprocessing

- **Generated log-mel spectrograms** from raw `.wav` audio files.
- **Padded**, **normalized**, and **resized** spectrograms to a standard size (128x128).
- **Data Augmentation**:  
  - Added Gaussian noise,  
  - Applied time-stretching,  
  - Performed pitch shifting.
- Saved preprocessed data for faster reloading and reusability.

### 3. Modeling

- **Model Architecture**:  
  - Base model: **ResNet-18** pretrained weights.
  - Modified first convolution layer to accept single-channel inputs.
  - Replaced the final fully-connected layer for 50-class classification.
- **Training Setup**:  
  - Optimizer: Adam  
  - Loss: CrossEntropyLoss  
  - Batch size: 64  
  - Early stopping and loss monitoring.
- **Training Phases**:
  - Trained on the original dataset.
  - Retrained on an augmented (expanded) dataset (~4x original size).

---

## 📊 Results

| Dataset           | Total Samples | Train Samples | Validation Samples | Test Samples | Train Acc | Val Acc | Test Acc |
|:------------------|:--------------:|:-------------:|:------------------:|:------------:|:---------:|:-------:|:--------:|
| Original          | 2000           | 1190          | 510                | 300          | 97.56%    | 66.27%  | -        |
| Original + Augmented | 8143        | 6921          | 1222               | 300          | 97.20%    | 98.28%  | **99.33%** |

✅ Final model achieved **99.33% accuracy** on the test set!

---

## 🧠 Why Not Use Vision Transformers (ViT)?

Although Vision Transformers could be considered, we decided against them because:
- Limited computational resources.
- The dataset is relatively small (only ~2,000 original samples).
- Audio clips are short (~5 sec), making long-term context modeling unnecessary.
- Our ResNet-18-based CNN already achieved excellent results.

---

## 📦 Installation

To run the project locally:

1. Clone the repository:
   ```bash
   git clone https://github.com/YehonatanRavoach/ESC50-DeepLearning.git
   cd ESC50-DeepLearning
2. Install required packages:
   ```bash
   torch>=2.0
   torchvision>=0.15
   numpy>=1.24
   pandas>=1.5
   librosa>=0.10
   matplotlib>=3.7
   seaborn>=0.12
   opencv-python>=4.7
   scikit-learn>=1.2

4. Download the ESC-50 dataset:
   ```bash
   python download_data.py
6. Run the notebooks step-by-step inside the notebooks/ folder.




