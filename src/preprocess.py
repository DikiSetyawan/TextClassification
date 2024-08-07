import pandas as pd 
import numpy as np
import re 
import csv
import time 
import os 
import datetime
from Sastrawi.Stemmer.StemmerFactory import StemmerFactory

def load_data(path):
    df = pd.read_csv(path)
    return df

def input_data():
    data = []
    while True:
        text = input("Input your text (or 'q' to stop): ")
        if text.lower() == 'q':
            break
        category = input("Input your category: ")
        timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        data.append([text, category, timestamp])

    file_path = '/home/sat/diki/topicClassification/data/data.csv'
    if not os.path.exists(file_path) or os.path.getsize(file_path) == 0:
        with open(file_path, 'w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(["Text", "Category"])  # header
    with open(file_path, 'a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)

def text_preprocess(text):
    #remove hashtags
    text = re.sub(r'#\w+'," ",text)
    #remove mentions
    text = re.sub(r'@\w+'," ",text)
    #remove urls
    text = re.sub(r'https?:\/\/\S+'," ",text)
    #remove emojis 
    emoji_pattern = re.compile("["
                               u"\U0001F600-\U0001F64F"  # emoticons
                               u"\U0001F300-\U0001F5FF"  # symbols & pictographs
                               u"\U0001F680-\U0001F6FF"  # transport & map symbols
                               u"\U0001F700-\U0001F77F"  # alchemical symbols
                               u"\U0001F780-\U0001F7FF"  # Geometric Shapes Extended
                               u"\U0001F800-\U0001F8FF"  # Supplemental Arrows-C
                               u"\U0001F900-\U0001F9FF"  # Supplemental Symbols and Pictographs
                               u"\U0001FA00-\U0001FA6F"  # Chess Symbols
                               u"\U0001FA70-\U0001FAFF"  # Symbols and Pictographs Extended-A
                               u"\U00002702-\U000027B0"  # Dingbats
                               u"\U000024C2-\U0001F251"  # Enclosed characters
                               "]+", flags=re.UNICODE)
    text = emoji_pattern.sub(r'', text)
    #remove punctuation
    text = re.sub(r'[^\w\s]'," ",text)
    #remove numbers
    text = text.replace('\n', ' ')
    text = re.sub(r'\d+', '', text)
    #lemmatizate
    factory = StemmerFactory()
    stemmer = factory.create_stemmer()
    text = stemmer.stem(text)
    text = re.sub(r'\b\w*f+[\w]*y+[\w]*p+[\w]*\b', '', text, flags=re.IGNORECASE)
    return text
    
def preprocess():
    df = load_data('/home/sat/diki/topicClassification/data/data.csv')
    df['Text'] = df['Text'].apply(text_preprocess)
    df.to_csv('/home/sat/diki/topicClassification/data/data.csv', index=False)

preprocess()