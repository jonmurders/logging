#Module to pull Dredge Data from archive
import pyodbc
import pandas as pd

#Data Type Selection, Options are CSV, or SQL
mode = 'CSV'
#CSV Inputs
path = './csvdemo.CSV'


#SQL inputs
server = '10.0.0.11'
database = ''
userid = ''
passwd = ''
table = ''
query = "SELECT * FROM "+table+" ORDER BY DateTime;"


def datapull(mode,path,server,database,userid,passwd,table,query):
    if mode == 'CSV':
        data = pd.read_csv(path)
        return data
    if mode == 'SQL':
        cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+database+';UID='+userid+';PWD='+passwd+'; Trusted_Connection=yes')
        data = pd.read_sql(query,cnxn)
    else:
        print('Error Retrieving Data')

test = datapull(mode,path,server,database,userid,passwd,table,query)