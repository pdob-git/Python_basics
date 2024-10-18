import pandas

df = pandas.read_csv("fakedata.csv")
df.to_excel('output_pandas.xlsx', sheet_name='Sheet1', index=False)
