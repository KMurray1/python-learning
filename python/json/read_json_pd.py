import pandas as pd

import json

f = open('data.json','r')
data = json.loads(f.read())

df = pd.json_normalize(data,record_path='records')

# print(df.head())


# orienting the dataframe around records can make it easier to work with in tools like Airflow.
print(df.head().to_json(orient='records'))