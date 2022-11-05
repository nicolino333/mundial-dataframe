#we make to clear of db
import pandas as pd
from dataclasses import replace


#we make to clear of db
db=pd.read_csv('df-mundial.csv',index_col=0)
print(db.head())
print(db.dtypes)
print(db.info())

#clear of colum name
col_name=db['name']
name=[]
no_deseado_name=['#','0','1','2','3','4','5','6','7','8','9']
for i in range(0,len(col_name)):
    jugador=str(col_name[i])
    for j in no_deseado_name:
        if j in jugador:
            jugador=jugador.replace(j,'')
    name.append(jugador)

#clear of colum high
col_high=db['high']
high=[]
no_deseado_high=['A','l','t','u','r','a',':']
for i in range(0,len(col_high)):
    high_=str(col_high[i])
    for j in no_deseado_high:
        if j in high_:
            high_=high_.replace(j,'')
    high.append(high_)
    
#clear of colum weight
col_weight=db['weight']
weight=[]
no_deseado_weight=['P','e','s','o',':']
for i in range(0,len(col_weight)):
    weight_=str(col_weight[i])
    for j in no_deseado_weight:
        if j in weight_:
            weight_=weight_.replace(j,'')
    weight.append(weight_)

#clear of colum age
col_age=db['age']
age=[]
no_deaseado_age=['E','d','a',':']
for i in range(0,len(col_age)):
    age_=str(col_age[i])
    for j in no_deaseado_age:
        if j in age_:
            age_=age_.replace(j,'')
    age.append(age_)
    
##we create a new dataframe cleared
del db['high']
del db['name']
del db['weight']
del db['age']
db['High']=high
db['Name']=name
db['Weight']=weight
db['Age']=age
new_db=db.reindex(columns=['Name','Weight','High','seleccion','Age'])
print(new_db.head())
#new_db.to_csv('MundialDataframe.csv')