import re

import pandas as pd

cartoon = pd.read_csv("cartoon_datasets.csv") 

#remove duplicates 
duplicates=cartoon.drop_duplicates()
print(duplicates)

#check for missing value
print(duplicates.isnull().sum())

#creating new column check wheather show is high or average
def rating_category(x):
    if x>8:
        return 'high'
    else:
        return 'average'
cartoon['rating_category']=cartoon['Rating'].apply(rating_category)
print(cartoon['rating_category'])

cartoon.to_csv('cleaned_cartoon.csv',index=False)
print(cartoon.head())
print("sucess")

df=pd.read_csv("cleaned_cartoon.csv")
print(df)

from sqlalchemy import create_engine

engine = create_engine(
    "mssql+pyodbc://Z14-55N\\SQLEXPRESS/testdb?driver=ODBC+Driver+17+for+SQL+Server&trusted_connection=yes"
)

df.to_sql('cartoons', con=engine, if_exists='replace', index=False)
print("Data loaded into SQL Server table 'cartoons'.")