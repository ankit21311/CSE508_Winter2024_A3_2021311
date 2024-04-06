import pandas as pd
import json

def parse(path):
    with open(path, 'r') as file:
        for line in file:
            yield json.loads(line)

def getDF(path):
    i = 0
    df = {}
    folder = parse(path)
    for d in folder:
        print(i)
        df[i] = d
        i += 1
    return df

# Use the correct file paths here
df = getDF('Electronics_5.json')
data_frame = pd.DataFrame.from_dict(df, orient='index')
data_frame.to_csv('data_frame.csv', index=False)

df = getDF('meta_Electronics.json')
meta_df = pd.DataFrame.from_dict(df, orient='index')
meta_df.to_csv('meta_data.csv', index=False, escapechar='\\')

data = pd.read_csv("data_frame.csv")
meta_data = pd.read_csv("meta_data.csv")

meta_data.head()
