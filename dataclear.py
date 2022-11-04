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
no_deseado_name=['#','0','1','2','3','4','5','6','7','8','9']
for i in range(0,len(col_name)):
    jugador=str(col_name[i])
    for j in no_deseado_name:
        if j in jugador:
            jugador=jugador.replace(j,'')
    name.append(jugador)


#clear of colum high
col_high=db['high']
print(col_high)
high=[]
no_deseado_high=['A','l','t','u','r','a',':']
for i in range(0,len(col_high)):
    high_=str(col_high[i])
    for j in no_deseado_high:
        if j in high_:
            high_=high_.replace(j,'')
    high.append(high_)
print(high[1])
    



#clear of colum weight
#col_weight=db['weight']
#weight=[]
#for j in range(0,len(col_weight)):
#    new_col_weight=col_weight[j].replace('P','').replace('e','').replace('s','').replace('o','').replace(':','')
#    weight.append(new_col_weight)

##we create a new dataframe cleared
#del db['high']
#del db['name']
#del db['weight']
#db['High']=high
#db['Name']=name
#db['Weight']=weight
#new_db=db.reindex(columns=['Name','Weight','High','seleccion','age'])
#print(new_db.head())
##new_db.to_csv('MundialDataframe.csv')#
