# 📧 Email Spam Classifier

This project is a machine learning-based **Email Spam Classifier** that identifies whether a given email is spam or not. It uses natural language processing (NLP) techniques to clean and analyze the text data and trains a classifier to make predictions.

## 🚀 Features

- 🧹 Text preprocessing: tokenization, stopword removal, stemming
- 📊 Feature extraction using TF-IDF
- 🧠 Trained with supervised learning (e.g., Naive Bayes / Logistic Regression)
- ✅ Predicts whether an email is **Spam** or **Ham (Not Spam)**
- 🖥️ Optional Streamlit or Flask-based web interface

## 🛠️ Tech Stack

- **Python 3**
- **Scikit-learn** – machine learning
- **Pandas, NumPy** – data handling
- **NLTK** – natural language processing
- **Streamlit / Flask** – optional UI

## 📂 Dataset

The model is trained on the [SMS Spam Collection Dataset](https://www.kaggle.com/datasets/uciml/sms-spam-collection-dataset) or a custom email dataset. Each entry includes:
- A label: `spam` or `ham`
- The email message text

## 🧪 ML Pipeline

1. **Text Cleaning & Preprocessing**
   - Lowercasing
   - Removing punctuation and special characters
   - Removing stopwords
   - Stemming

2. **Feature Extraction**
   - Convert text into numerical format using **TF-IDF**

3. **Model Training**
   - Naive Bayes / Logistic Regression
   - Train-test split and model evaluation

4. **Evaluation Metrics**
   - Accuracy
   - Precision, Recall, F1-score
   - Confusion Matrix

## 💻 How to Run

1. **Clone the repo**
   ```bash
   git clone https://github.com/yourusername/email-spam-classifier.git
   cd email-spam-classifier
