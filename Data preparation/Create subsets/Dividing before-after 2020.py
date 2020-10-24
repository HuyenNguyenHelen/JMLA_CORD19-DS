
# Dividing each data release based on paper published after and before Dec2020
# Import essential libraries
import pandas as pd
import re

# Open each metadata files of all wanted data releases
paths=["/metadata-March13.csv", "/metadata-April3.csv", "/metadata-May12.csv", "/metadata-Jun5.csv", "/metadata-Jul5.csv", "/metadata-Aug5.csv" ]
for i in range(len(paths)):
    with open(paths[i], "r",  newline="", encoding='utf-8') as file:
        df= pd.read_csv(file)
    before = []
    after = []
    # Iterate to classify papers published before and after 2020
    for id, abstr, year, pdf, pmc in zip(df['cord_uid'], df['abstract'], df['publish_time'], df['pdf_json_files'], df['pmc_json_files']):
        if re.search("(202\d{1})", str(year)):
            after.append([id, abstr, year, pdf, pmc])
        else:
            before.append([id, abstr, year, pdf, pmc])
    # Save classified lists to CSV
    df_before = pd.DataFrame(before,columns=['cord_uid','abstract','publish_time', 'pdf_json_files', 'pmc_json_files'])
    df_after = pd.DataFrame(after, columns=['cord_uid', 'abstract', 'publish_time', 'pdf_json_files', 'pmc_json_files'])
    with open("/before2020"+str(i)+".csv", "w", newline="", encoding='utf-8') as file:
        df_before.to_csv(file)
    with open("/after2020"+str(i)+".csv", "w", newline="", encoding='utf-8') as f:
        df_after.to_csv(f)


