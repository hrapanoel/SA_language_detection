import sys
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.linear_model import Perceptron
from sklearn.pipeline import Pipeline
from sklearn.datasets import load_files
from sklearn.model_selection import train_test_split
from sklearn import metrics
from sklearn.naive_bayes import MultinomialNB
import re
import numpy as np
import pandas as pd
from sklearn.externals import joblib
from ipywidgets import widgets
from IPython.display import display

language_code = {'afr':1, 'nbl':2, 'nso':3, 'sot':4, 'ssw':5, 'tso':6, 'tsn':7, 'ven': 8, 'xho':9,
'zul':10, 'eng':11}
#code = dict((v,k) for k,v in language_code.items())
code = {1: 'Afrikaans', 2:'Ndebele', 3: 'Sepedi', 4: 'Sesotho', 5: 'Siswati',
       6: 'Tsonga', 7: 'Tswana', 8: 'Venda', 9: 'Xhosa', 10: 'Zulu', 11: 'English'}

# regex to replace all numerics
replace_numbers=re.compile(r'\d+',re.IGNORECASE)

def clean_text(input_text):
    text = input_text.lower()
    text = replace_numbers.sub('', text)

    text = text.replace('ã…â¡', 'š')
    text = text.replace('ï¿½', '')
    text = text.replace('ª', '')

    # All special characters are kept.
    return text

pipe = joblib.load('./language_detect.joblib') 
outputText = widgets.Textarea(description='Language:')

inputText = widgets.Text(placeholder='Type text here',
    description='Input text:',
    disabled=False)

def predict_sentences(sender):
    sentences = [text for text in inputText.value.split("\n")]
    cleaned_sentence = [clean_text(text) for text in sentences]
    predicted_languages = pipe.predict(cleaned_sentence)
    outputText.value = code[predicted_languages[0]]
#     for sentence, lang in zip(sentences, predicted_languages):
#         outputText.value = u'{} ----> {}'.format(sentence, code[lang])

    
inputText.on_submit(predict_sentences)
container = widgets.VBox([inputText, outputText])
