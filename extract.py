import pandas as pd

print("Extract data")

data={
    'Id': [101,102,103],
    'Name': ['Ram','Raj','Rach'],
    'Age': [23,45,37]
}

df=pd.DataFrame(data)
print(df)