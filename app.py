import pickle
import streamlit as st
from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.pipeline import Pipeline
from sklearn.feature_extraction.text import TfidfVectorizer
from xgboost import XGBClassifier

def character_tokenizer(text):
    return [x for x in text]

with open('model.pkl', 'rb') as f:
    model = pickle.load(f)

def predict(model, sentence):
	output = model.predict([sentence])
	result = output.item()

	categories = {
		0: "WEAK",
		1: "NORMAL",
		2: "STRONG",
	}

	return st.success('PASSWORD IS ' + categories.get(result))

st.title('PASSWORD STRENGTH')
text = st.text_input('...')
res = st.button('PREDICT')

if res:
	predict(model, text)
