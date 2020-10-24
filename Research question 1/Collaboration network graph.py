# Prepare proper files as input to create collaboration network graph in Gephi

# Import essential library
import pandas as pd

# Open file to read
with open(r"path\collaborations_ranked.csv", 'r', encoding='utf-8') as file:
    df = pd.read_csv(file)

# Generate Nodes
# Create ID for each affiliation
id_label = [i for i, j in enumerate(df.label)]
df['id'] = id_label

# Save ID list to CSV
new_df = pd.DataFrame(list(zip(df.id, df.label)),
                      columns=['id', 'label'])
with open(r"\collaborations_nodes.csv", 'w', newline='',
          encoding='utf-8') as file:
    new_df.to_csv(file)

# Open the file containing all collaborations
with open(r"\collaborations_list.csv", 'r', encoding='utf-8') as file:
    df2 = pd.read_csv(file)

# Map ID of affiliations with collaboration tuples
# Map ID with "source" affiliation
source_list = []
for s in df2.source:
    for i, v in zip(new_df.id, new_df.label):
        if s == v:
            source_list.append(i)

# Map ID with "target" affiliation
target_list = []
for t in df2.target:
    for i, v in zip(new_df.id, new_df.label):
        if t == v:
            target_list.append(i)

# Save tuples of source ID and target ID to CSV
data = pd.DataFrame(list(zip(source_list, target_list)), columns=['source', 'target'])
with open(r"\collaborations_edges.csv", 'w', newline='', encoding='utf-8') as file:
    data.to_csv(file)