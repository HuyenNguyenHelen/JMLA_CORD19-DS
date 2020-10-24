#Import essential libraries
import pandas as pd
from wordcloud import WordCloud, STOPWORDS
import matplotlib.pyplot as plt
# Download stopwords
stopwords = set(STOPWORDS)

# Open all csv files of DS1
paths= ["\path\pdf_reformatted.csv", "\path\pmc_reformatted.csv"]

all_affi = []
for path in paths:
    with open(path, "r",  newline="", encoding='utf-8') as file:
        df= pd.read_csv(file)
    # Clean digits,symbols, and lowercase
    df['affiliations'] = df['affiliations'].apply(lambda x: " ".join(x for x in str(x).split() if not x.isdigit() and not x.isspace()))
    df['affiliations'] = df['affiliations'].str.replace('[^\w\s,]', '')
    df['affiliations'] = df['affiliations'].str.lower()
    # Extract affiliations of each paper
    for affi_list in df['affiliations'].dropna():
        all_affi.append([item for item in affi_list.split(",") if not None])

# Extract collaborations in each paper
collaboration = []
for affi_list in all_affi:
    if affi_list:
        i = affi_list[0]
        for j in affi_list[1:]:
            if i.strip() != j.strip():
                if i.strip() != None or j.strip() != None:
                    if len(i ) >5 and len(j ) >5:
                        l = [i.strip(), j.strip()]
                        tup = tuple(l)
                        collaboration.append(tuple(l))
                    else:
                        pass

print(len(collaboration))

# Save the list of collaborations to CSV
df_collaboration =pd.DataFrame(collaboration, columns = ['x' ,'y'])
with open (r"path\collaborations_list.csv", 'w', encoding='utf-8') as file:
    df_collaboration.to_csv(file)

# Count number of collaborations
hist ={}
for tup in collaboration:
    for item in tup:
        hist[item ] =hist.get(item, 0 ) +1

# Rank the number of collaborations
sorted_hist = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}

# Save the ranked collaboration dictionary to CSV
colla_ranked =pd.DataFrame.from_dict (sorted_hist ,orient = 'index', columns = ['Number of collaborations'])
with open ("path\collaborations_ranked_DSApr17.csv", 'w',  newline="", encoding='utf-8') as file:
    colla_ranked.to_csv(file)



