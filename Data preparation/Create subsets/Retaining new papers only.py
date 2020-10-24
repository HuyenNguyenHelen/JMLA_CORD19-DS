# Import essential library
import pandas as pd

paths=["/after2020-March13.csv", "/after2020-April3.csv", "/after2020-May12.csv", "/after2020-Jun5.csv", "/after2020-Jul5.csv", "/after2020-Aug5.csv" ]
i=0
while i<len(paths)-1:
    if i+1>len(paths):
        break
    else:
    #Open after2020 subset of each data release
    with open(paths[i], "r", encoding='utf-8') as f:
        data1 = pd.read_csv(f)
    # Open after2020 subset of next data release
    with open(path[i+1], "r", newline="", encoding='utf-8') as f:
        data2 = pd.read_csv(f)
    i+=1
    oldDoc = [doc for doc in data1["cord_uid"]]
    newDoc = []
    for id, abstr, year, pdf, pmc in zip(data2['cord_uid'], data2['abstract'], data2['publish_time'], data2['pdf_json_files'], data2['pmc_json_files']):
        if id not in oldDoc:
            newDoc.append([id,abstr, year, pdf, pmc])
    # Save newly updated subset to CSV
    df_newOnly = pd.DataFrame(newDoc, columns=['cord_uid','abstract','publish_time', 'pdf_json_files', 'pmc_json_files'])
    with open("/after2020_newOnly"+str(i)+".csv", "w",  newline="", encoding='utf-8') as f:
        df_newOnly.to_csv(f)