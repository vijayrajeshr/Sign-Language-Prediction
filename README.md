# 🤟 Sign Language Prediction

A complete deep learning pipeline for real-time American Sign Language (ASL) alphabet recognition using a webcam and CNN-based classifier.

---

## 📄 Project Overview

This project captures sign language hand gestures, processes them into a dataset, trains a classifier, and performs real-time inference. It aims to assist in bridging communication gaps for the hearing and speech-impaired.

---

## 📂 Repository Structure

- **collect_imgs.py** - Captures labeled gesture images via webcam.
- **create_dataset.py** - Processes and prepares image data for training.
- **train_classifier.py** - Trains a CNN model on the dataset.
- **inference_classifier.py** - Runs real-time gesture recognition using the trained model.
- **graph.py** - (Optional) Plots training graphs (accuracy/loss).
- **model.p** - Saved trained model file.
- **data.pickle** - Serialized labels and dataset.
- **LICENSE** - MIT License for open-source use.

---

## 📘 Documentation

Refer to the provided PDF (`sign-language-prediction.pdf`) for a complete explanation of the project pipeline, model architecture, data flow, and results.

---

## ✅ Status

Fully functional. Real-time gesture recognition via webcam is working and tested.

---

## 📬 Contact

For queries, feedback, or collaboration:  
**your.email@example.com**

---

## 📜 License

This project is licensed under the **MIT License**.
