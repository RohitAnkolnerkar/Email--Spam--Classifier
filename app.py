import streamlit as st
import pickle
import support
import pandas as pd
import numpy as np
model=pickle.load(open('model-Copy1.pkl','rb'))
tfidf=pickle.load(open('vectorizer.pkl','rb'))
st.title("Email/Spam Classifier")

input1 =st.text_input('Enter the message')
if st.button('predict'):
    transform_sms = support.transform_text(input1)
    vector = tfidf.transform([transform_sms])
    result = model.predict([vector])[0]
    if result == 1:
        st.header('spam')
    if result == 0:
        st.header("ham")


