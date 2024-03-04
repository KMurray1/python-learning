import pandas as pd

data = {'Name':['Paul','Bob','Susan','Bill'],
        'Age':[23,19,40,51]}

df = pd.DataFrame(data)

df.to_csv('fromdf.csv',index=False)