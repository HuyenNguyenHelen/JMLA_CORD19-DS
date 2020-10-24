# Import essential libraries
import pandas as pd
from nltk.tokenize import RegexpTokenizer
from stop_words import get_stop_words
from nltk.stem.porter import PorterStemmer
import gensim
import gensim.corpora as corpora
from gensim.models import CoherenceModel

# open file to read abstracts
with open(r"path/metadata-Aug5.csv", "r", encoding='utf-8') as file:
    df= pd.read_csv(file)

# Clean text by removing numbers, symbols
df['abstract']=df['abstract'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
df['abstract']=df['abstract'].str.replace('[^\w\s,]','')

# Create Tokenizer
tokenizer = RegexpTokenizer(r'\w+')

# Create English stop words list
en_stop = get_stop_words('en')
stop_plus = ['word', 'count', 'text', 'all', 'right', 'no', 'without', 'abstract', 'no', 'reuse', 'without', 'abstract', 'nan']

# Create PorterStemmer
p_stemmer = PorterStemmer()

# Create list of documents
abstract_set = []
for abstract in df['abstract'].dropna():
    abstract_set.append(abstract)

# Create a list of tokenized and stemmed documents
texts = []
for i in abstract_set:
    # Lowercase tokenize document string
    raw = i.lower()
    tokens = tokenizer.tokenize(raw)
    # Remove stop words from tokens
    stopped_tokens = [i for i in tokens if not i in en_stop + stop_plus]
    # Stem tokens
    stemmed_tokens = [p_stemmer.stem(i) for i in stopped_tokens if len(i)>3]
    texts.append(stemmed_tokens)

# Turn our tokenized documents into a id - term dictionary
dictionary = corpora.Dictionary(texts)

# Convert tokenized documents into a document-term matrix
corpus = [dictionary.doc2bow(text) for text in texts]

# Generate LDA model
ldamodel = gensim.models.ldamodel.LdaModel(corpus, num_topics=30, id2word = dictionary, passes=60)

# Get topics from results
topics = []
for topic in ldamodel.print_topics(num_topics=30,num_words=12):
    topics.append(topic)
print(topics)

# Save topics to CSV
df_topics = pd.DataFrame(topics)
with open ("/LDAgensim_wholeDS.csv", 'w',  newline="", encoding='utf-8') as file:
   df_topics.to_csv(file)

# Compute Coherence Score
coherence_ldamodel = CoherenceModel(model=ldamodel, texts=texts, dictionary=dictionary, coherence='c_v')
coherence_lda = coherence_ldamodel.get_coherence()
print('Coherence Score: ', coherence_lda)