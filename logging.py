import dredgespec
import datainput
import pandas as pd 

data = datainput.datapull(datainput.mode,datainput.path,datainput.server,datainput.database,datainput.userid,datainput.passwd,datainput.table,datainput.query)

print(data.head)