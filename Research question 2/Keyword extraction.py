# Import essential libraries
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
from nltk.stem import WordNetLemmatizer
import yake
stopwords = set(STOPWORDS)
lemmatizer = WordNetLemmatizer()

# Open file to read abstracts
with open(r"path\metadata.csv", "r",  encoding='utf-8') as file:
    df= pd.read_csv(file)
file.close()

# Tokenize and lemmatize abstracts
text=''
for abstr in df['abstract'].dropna():
    for w in abstr.split():
        if w not in stopwords:
            text=text+' '+ str(lemmatizer.lemmatize(w))

# Specify parameters
language = "en"
max_ngram_size = 3
deduplication_thresold = 0.9
deduplication_algo = 'seqm'
windowSize = 1
numOfKeywords =40

# Yake model with specified parameters
custom_kw_extractor = yake.KeywordExtractor(lan=language, n=max_ngram_size,  dedupLim=deduplication_thresold, dedupFunc=deduplication_algo, windowsSize=windowSize, top=numOfKeywords, features=None)
keywords = custom_kw_extractor.extract_keywords(text)

# Save results to CSV
df_keywords = pd.DataFrame(keywords)
with open (r"path\YAKEkeywords_3gram.csv", 'w',  newline="", encoding='utf-8') as file:
   df_keywords.to_csv(file)
