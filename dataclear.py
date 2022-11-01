#we make to clear of db
import pandas as pd
from dataclasses import replace


#we make to clear of db
db=pd.read_csv('df-mundial.csv',index_col=0)
#print(db.head())
#print(db.dtypes)
#print(db.info())

#clear of colum name
col_name=db['name']
name=[]
for j in range(0,len(col_name)):
    new_col_name=col_name[j].replace('#','').replace('0','').replace('1','').replace('2','').replace('3','').replace('4','').replace('5','').replace('6','').replace('7','').replace('8','').replace('9','')
    name.append(new_col_name)

#clear of colum high
col_high=db['high']
high=[]
for j in range(0,len(col_high)):
    new_col_high=col_high[j].replace('A','').replace('l','').replace('t','').replace('u','').replace('r','').replace('a','').replace(':','')
    high.append(new_col_high)

#clear of colum weight
col_weight=db['weight']
weight=[]
for j in range(0,len(col_weight)):
    new_col_weight=col_weight[j].replace('P','').replace('e','').replace('s','').replace('o','').replace(':','')
    weight.append(new_col_weight)

#we create a new dataframe cleared
del db['high']
del db['name']
del db['weight']
db['High']=high
db['Name']=name
db['Weight']=weight
new_db=db.reindex(columns=['Name','Weight','High','seleccion','age'])
print(new_db)
new_db.to_csv('MundialDataframe.csv')
