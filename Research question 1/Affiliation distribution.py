# Import essential libraries
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
stopwords = set(STOPWORDS)

# Open file to read
paths= ["\path\pdf_reformatted.csv", "\path\pmc_reformatted.csv"]
affiliations = ''
for path in paths:
    with open(path, "r",  newline="", encoding='utf-8') as file:
        df= pd.read_csv(file)
    # Clean digits,symbols, and lowercase
    df['affiliations'] = df['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
    df['affiliations'] = df['affiliations'].str.replace('[^\w\s,]', '')
    df['affiliations'] = df['affiliations'].str.lower()
    # Create a string of institutions
    for inst in df['affiliations'].dropna():
        affiliations = affiliations + str(inst)

# Count frequency of affiliation
hist = dict()
for inst in affiliations.split(','):
    if len(inst.strip()) > 4:
        hist[inst.strip()] = hist.get(inst.strip(), 0) + 1

print(len(hist.keys()))

# Rank frequency of affiliations
auth_inst_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}

# Save the ranked list into a csv file
rank_affi = pd.DataFrame.from_dict(auth_inst_sorted, orient='index', columns=['count'])
with open (r"path\affiliation_frequency.csv", 'w',  newline="", encoding='utf-8') as file:
    rank_affi.to_csv(file)
