from sklearn.feature_extraction.text import TfidfVectorizer
import pandas as pd
from sklearn.metrics.pairwise import cosine_similarity
import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

#tokenize, lemmatize and remove stopwords to clean text
def filter_text(text):
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    tokens = nltk.word_tokenize(text)
    lemmatizer = WordNetLemmatizer()
    clean_tokens = [lemmatizer.lemmatize(token) for token in tokens if token not in stopwords.words('english')]
    return ' '.join(clean_tokens)

#concatenate all columns into one so we can use it for tfidf
df = pd.read_csv('archive/random_sample.csv')
text_data = df.apply(lambda row: ' '.join(row.values.astype(str)), axis=1)
text_data = text_data.apply(filter_text)

#apply tfidf on dataset
vectorizer = TfidfVectorizer(ngram_range=(1, 2), stop_words='english')
tfidf_matrix = vectorizer.fit_transform(text_data)

#user input
while True:
    print("Type 'exit' to quit")
    user_input = input("Enter Query: ")
    if user_input.lower() == 'exit':
        break
    user_input_filter = filter_text(user_input)
    user_input_tfidf = vectorizer.transform([user_input_filter])

    #calculate cosine similarity
    cosine_similarities = cosine_similarity(user_input_tfidf, tfidf_matrix).flatten()
    top_indices = cosine_similarities.argsort()[-5:][::-1]

    #print recommendations
    print("Top 5 movie recommendations based on your input:")
    for index in top_indices:
        print(df.iloc[index]["title"])