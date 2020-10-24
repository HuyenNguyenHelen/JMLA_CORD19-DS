# Import essential libraries
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import gensim.corpora as corpora
from gensim.models import ldaseqmodel

# Create a Tokenizer
tokenizer = RegexpTokenizer(r'\w+')

# create English stop words list
en_stop = get_stop_words('en')
stop_plus = ['word', 'count', 'text', 'all', 'right', 'no', 'without', 'abstract', 'no', 'reuse', 'without', 'abstract',
             'nan']

# Create PorterStemmer
p_stemmer = PorterStemmer()

# open metadata file and cleaning
paths = [r"\after2020_DS1.csv", r"\after2020_newOnly_Ap3.csv",
         r"\after2020_newOnly-May5.csv", r"\after2020_newOnly-Jun5.csv",
         r"\after2020_newOnly-Jul5.csv", r"\after2020_newOnly-Aug5.csv"]

abstract_set = []
for i in range(0, len(paths)):
    with open(path[i], "r", encoding='utf-8') as file:
        df = pd.read_csv(file)
    df['abstract'] = df['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
    df['abstract'] = df['abstract'].str.replace('[^\w\s,]', '')
    # create list of documents
    for abstract in df['abstract'].dropna():
        abstract_set.append(abstract)

# Tokenize documents by looping through document list
texts = []
for i in abstract_set:
    # clean and tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop + stop_plus]
    # stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens if len(i) > 3]
    texts.append(stemmed_tokens)

# Create a id dictionary of tokenized documents
dictionary = corpora.Dictionary(texts)

# Convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# Generate the model
time_slice = [len(df1), len(df2), len(df3), len(df4), len(df5), len(df6)]
ldaseq = ldaseqmodel.LdaSeqModel(corpus=corpus, id2word=dictionary, time_slice=time_slice, num_topics=15)

# Get topics of each slice from the result
topics = []
i = 0
while i < 6:
    topic_i = []
    for topic in ldaseq.print_topics(time=i, top_terms=12):
        topic_i.append(topic)
    topics.append(topic_i)
    i += 1

# Save topics to CSV
df_topics = pd.DataFrame(topics)
with open(r"\path\DTM_6timeslices.csv", 'w', newline="", encoding='utf-8') as file:
    df_topics.to_csv(file)


