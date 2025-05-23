import nltk
from nltk.corpus import stopwords
import string
from nltk .stem.porter import PorterStemmer
ps=PorterStemmer()
nltk.download('punkt')

import pandas as pd
import numpy as np
def transform_text(text):
    text = text.lower()
    text = nltk.tokenize.word_tokenize(text)
    y = []
    for i in text:
        if i.isalnum():
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)
    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))

    return " ".join(y)
