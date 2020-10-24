# Extract tarfile
# Import packages
import os
import json
import pandas as pd
import tarfile

# Open tar file to extract
my_tar = tarfile.open("\pmc_custom_license.tar.gz")
my_tar.extractall("\path\DS_extracted")  # specify which folder to extract to
my_tar.close()

# Integrate the Json files and reformat them into two CSV file
# Iterate to open and read all json files in folder

# First directory
dir1 = r"\path\document_parses\pmc_json"
filenames1 = os.listdir(dir1)
print("Number of articles retrieved from :", len(filenames1))

#Second directory
dir2 = r"\path\comm_use_subset\pmc_json"
filenames2 = os.listdir(dir2)
print("Number of articles retrieved from :", len(filenames2))

# Store content of all json files from two dirs in a list
all_files = []
for filename in filenames1:
    filename = os.path.join(dir1, filename)
    filename.encode('unicode-escape')
    file = json.load(open(filename, 'rb'))
    all_files.append(file)

for filename in filenames2:
    filename = os.path.join(dir2, filename)
    filename.encode('unicode-escape')
    file = json.load(open(filename, 'rb'))
    all_files.append(file)



# Extract all needed content
# Extract paperids and paper titles
paper_id = [file['paper_id'] for file in all_files]
titles = [file['metadata']['title'] for file in all_files]

# Extract author_names, affiliations, abstract_text, body_text
author_names, affiliations, body_text = [], [], []
authors = [file['metadata']['authors'] for file in all_files]
for element in authors:
    author_names.append([item['first'] + " " + item['last'] for item in element])
    try:
        affiliations.append([item['affiliation']['institution'] for item in element])
    except:
        affiliations.append(None)

bodies = [file["body_text"] for file in all_files]
for body in bodies:
    text = [para['text'] for para in body]
    body_text.append(text)

formated_data = {'paper_id': paper_id, 'title': titles, 'authors_names': author_names, 'affiliations': affiliations,
                  'text': body_text}

#Save the dataset into a CSV file
df = pd.DataFrame.from_dict(formated_data, orient='columns')
with open(r"\path\reformatted.csv", "w", newline="", encoding='utf-8') as file:
    df.to_csv(file)

