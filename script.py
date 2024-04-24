import re
from collections import Counter
import nltk
from nltk.corpus import stopwords

nltk.download('stopwords')

def preprocess_text(text):
    text = re.sub(r'[^a-zA-Z\s]', '', text).lower()
    tokens = text.split()
    stop_words = set(stopwords.words('english'))
    tokens = [token for token in tokens if token not in stop_words]
    return tokens

def count_word_frequency(tokens):
    word_freq = Counter(tokens)
    return word_freq

with open('paragraphs.txt', 'r') as file:
    text = file.read()

processed_text = preprocess_text(text)

word_freq = count_word_frequency(processed_text)

for word, freq in word_freq.items():
    print(f"{word}: {freq}")
