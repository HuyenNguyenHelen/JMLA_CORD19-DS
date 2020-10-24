# Import essential libraries
from wordcloud import STOPWORDS
import pandas as pd
# Download stopwords
stopwords = set(STOPWORDS)

# Open metadata file
with open(r"path\metadata.csv","r", encoding='utf-8')as file:
    df= pd.read_csv(file)

# Count the number of publications
hist=dict()
for journal in df['journal'].dropna():
    hist[journal.strip()]=hist.get(journal.strip(),0)+1

# Rank the number of publications
journals_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}

# Save the ranked publication dictionary to CSV
journals_ranked=pd.DataFrame.from_dict (journals_sorted,orient = 'index', columns = ['count'])
with open (r"\Journals_frequency.csv", 'w',  newline="", encoding='utf-8') as file:
    journals_ranked.to_csv(file)


# THE NUMBER OF PUBLICATIONS OVER YEARS
# Import essential library
import re

# Extract publication years
dates = ''
for date in df['publish_time'].dropna():
    dates = dates + " " + str(date)
# Extract publication years after 2000
years = re.findall("(20\d{2})", dates)
# Extract publication years before 2000
years.extend(re.findall("(19\d{2})", dates))

# Count the number of publication years
hist = {}
for year in years:
    hist[year] = hist.get(year, 0) + 1

# Rank the number of publication years
years_val_sorted = {k: v for k, v in sorted(hist.items(), key=lambda item: item[1], reverse=True)}

# Save ranked publication years to CSV
years_ranked = pd.DataFrame.from_dict(years_val_sorted, orient='index', columns=['quantity'])
with open (r"\Journals_overYears_DSApr17.csv", 'w',  newline="", encoding='utf-8') as file:
    years_ranked.to_csv(file)

