#!/usr/bin/env python
# coding: utf-8

# In[5]:


## Import Library
from IPython.display import display
from sqlalchemy import create_engine
import pandas as pd
from datetime import datetime


# In[6]:


## Load Data

transactions = pd.read_csv("../transactions.csv")
customers = pd.read_csv("../customers.csv")
products = pd.read_csv("../products.csv")

print("=== Data Loaded ===")
print(f"Transactions: {transactions.shape}")
print(f"Customers: {customers.shape}")
print(f"Products: {products.shape}\n")


# In[7]:


## Ubah type data column timestamp pada transaction menjadi datetime
transactions['timestamp'] = pd.to_datetime(transactions['timestamp'], errors='coerce')


# In[8]:


## Exclude quantity yang null pada column transaction
transactions = transactions.dropna()


# In[9]:


## Merged Data
merged = (
    transactions.merge(customers, on="customer_id", how="left")
    .merge(products, on="product_id", how="left")
)


# In[10]:


## Buat column price dan month
merged["total_price"] = merged["quantity"] * merged["price"]
merged["month"] = merged["timestamp"].dt.to_period("M").astype(str)


# In[11]:


merged.sample(5)


# In[12]:


## Ingest to database

server = 'localhost'
database = 'ecommerce'
username = 'sa'               # user SQL Server
password = 'admin'  # password login SQL Server
table = 'analytic'

# Driver bawaan SQL Server (pastikan sudah terinstall ODBC)
connection_string = f"mssql+pyodbc://{username}:{password}@{server}/{database}?driver=ODBC+Driver+17+for+SQL+Server"
engine = create_engine(connection_string)


# In[13]:


merged.to_sql(
    name=table,
    con=engine,
    if_exists='replace',# bisa diganti 'append' kalau mau nambah data
    index=False
)


# In[14]:


cek = """
SELECT COUNT(*) AS total_rows
FROM ecommerce.dbo.analytic
"""

df = pd.read_sql_query(cek, con=engine)
df.head()


# In[ ]:




