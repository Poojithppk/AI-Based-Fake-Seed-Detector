**#AI Based Fake Seed Detector**
**Problem Statement**
Fake and non viable seeds are often sold as genuine seeds.
This causes crop failure and financial loss to farmers.
Manual verification is difficult and laboratory methods are costly.
This project aims to detect fake or spoiled pea seeds using image based deep learning.
**Objective**
Identify genuine and fake pea seeds from images
Reduce the risk of fake seeds being classified as genuine
Provide fast prediction using a simple web application
**Dataset**
Crop Pea seeds
Total images 5513
Genuine seed images 1200
Spoiled or fake seed images 4311
Dataset was used as it is for model training.
**The dataset link is provided in
dataset_link.txt**
**Model and Methodology**
Deep learning based image classification approach
Pretrained EfficientNet model used
Input image size 224 x 224
Binary classification
Genuine seed
Fake or spoiled seed
The model learns visual features such as color texture and surface patterns.
Precision was prioritized to avoid classifying fake seeds as genuine.
**Results**
High precision achieved on validation data
Stable performance under different image conditions
Inference time less than 2 seconds on CPU
**Deployment**
Model trained using Google Colab
Deployed using Streamlit
The application allows
Uploading a seed image
Viewing prediction result
Viewing confidence score

AI-Based-Fake-Seed-Detector/
|
|-- app.py
|-- Fake_seed_detector.ipynb
|-- seed_model.h5
|-- requirements.txt
|-- dataset_link.txt
|-- FAKE SEED DETECTOR.pptx
|-- README.md
