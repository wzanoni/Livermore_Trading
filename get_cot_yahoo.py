

 
import pandas as pd
import requests
from bs4 import BeautifulSoup

res = requests.get('https://br.financas.yahoo.com/quote/%5EBVSP/history?p=%5EBVSP')
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))
print(df[0].to_json(orient='records'))


df1 = df['Data'].tolist()



res = requests.get('https://br.financas.yahoo.com/quote/%5EBVSP/history?p=%5EBVSP')
soup = BeautifulSoup(res.content,'lxml')
table = soup.find_all('table')[0] 
df = pd.read_html(str(table))[0]
dt       = df["Data"].tolist()
abertura = df["Abrir"].tolist()

df_cot = pd.DataFrame()
df_cot = df
df_cot.head()
    