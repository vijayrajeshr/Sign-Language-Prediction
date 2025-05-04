# Sign Language Prediction 🤟

A deep learning-based system for real-time American Sign Language (ASL) alphabet recognition using a webcam and Convolutional Neural Networks (CNN).

## 🚀 Overview

This project enables live ASL hand gesture recognition, translating static signs into text using a custom-trained CNN model. It includes tools for data collection, preprocessing, training, and real-time inference.

## 📁 Repository Structure

- `collect_imgs.py` – Capture labeled gesture images via webcam.
- `create_dataset.py` – Process and convert images into a structured dataset.
- `train_classifier.py` – Train the CNN classifier.
- `inference_classifier.py` – Perform real-time ASL prediction.
- `graph.py` – Visualize training metrics (accuracy/loss).
- `model.p` – Saved trained model.
- `data.pickle` – Serialized labels and data features.
- `LICENSE` – Project license information.

## 📘 Documentation

Detailed explanation of the pipeline, architecture, and methodology is available in the [`sign-language-prediction.pdf`](./sign-language-prediction.pdf).

## 📄 License

This project is licensed under the [MIT License](./LICENSE) 📝

Questions and doubts are welcomed here.
