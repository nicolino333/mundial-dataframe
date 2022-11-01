#we will use 5 boockstore
from bs4 import BeautifulSoup
import requests
import lxml
from lxml import html
import pandas as pd


#we stract the selecciones's links
try:
    url='https://www.fichajes.com/mundo/copa-mundial/clasificacion'
    url_base='https://www.fichajes.com'
    peticion=requests.get(url)
    if peticion.status_code==200:
       htm_pagina=BeautifulSoup(peticion.text,'lxml')
       links=htm_pagina.find('div',attrs={'class':"topLogos topLogos--groupTeams"}).find_all('li')
       lista_links_selecciones=[]
       for i in range(0,len(links)):
           k=links[i].a.get('href')
           link=url_base+k
           lista_links_selecciones.append(link)            
    else:
        raise ValueError(f'Error: {peticion.status_code}')
except ValueError as ve:
    print(ve)



#function for extract the plantilla of countrys each on of lista_links , return one links of player
def plantilla_selecciones(lista_links_selecciones):
    try:        
        peticion=requests.get(lista_links_selecciones)
        if peticion.status_code==200:
            #we stract the link of all player
            html_plantilla=peticion.content.decode('utf-8')
            est=html.fromstring(html_plantilla)
            links2=est.xpath('//td[@class="classement__player"]/a/@href')
            links_jugadores=[]
            for i in range(0,len(links2)):
                jugador=url_base+links2[i]
                links_jugadores.append(jugador)
            return links_jugadores                
        else :
            raise ValueError(f'Error: {peticion.status_code}')
    except ValueError as ve:
        print(ve)


#function for extract each of link , the data of players
def jugadores(links_jugadores):
    try:
        peticion=requests.get(links_jugadores)
        if peticion.status_code==200:
            #we stract the name
            html_pag=BeautifulSoup(peticion.text,'lxml')
            listas=html_pag.find('div',attrs={'class':"title"}).find_all('h1')
            nombre=listas[0].text
            #we stract age , high and weight 
            datos=html_pag.find('ul',attrs={'class':'bio__infos'}).find_all('li')
            datos.pop(0)
            info=[]
            for i in range(0,3):
                dato=datos[i].get_text().replace(' ','').replace('\n','')
                info.append(dato)
            #we stract the nationality of the player
            nacionalidad=html_pag.find('span',attrs={'class':"nationality"}).get_text()
            seleccion=nacionalidad.replace(' ','').replace('\n','')
            #dictionary of players
            jugador={'nombre':nombre,
                    'edad':info[0],
                    'altura':info[1],
                    'peso':info[2],
                    'seleccion':seleccion
            }
            return jugador
            
        else:
            raise ValueError(f'Eror: {peticion.status_code}')
    except ValueError as Ve:
        print(Ve)


try:
    #this bucle retorn one list of plantillas of the 32 countrys
    seleccionados=[]
    for i in range(0,len(lista_links_selecciones)):
        jugadores_=plantilla_selecciones(lista_links_selecciones[i])
        seleccionados.append(jugadores_)
    #we make the data frame of all players of the selecciones
    nombre=[]
    edad=[]
    altura=[]
    peso=[]
    seleccion=[]
    for j in range (0,len(seleccionados)):
        pais=seleccionados[j]
        for i in range(0,len(pais)):
            data_jugadores=jugadores(pais[i])
            nombre.append(data_jugadores['nombre'])
            edad.append(data_jugadores['edad'])
            altura.append(data_jugadores['altura'])
            peso.append(data_jugadores['peso'])
            seleccion.append(data_jugadores['seleccion'])
    #dictionary of dataframe is made , just there make the db
    data_frame={'name':nombre,
                 'age':edad,
                 'high':altura,
                 'weight':peso,
                'seleccion':seleccion,
                }
    print(data_frame)

except ValueError as Ve:
    print(Ve)

df=pd.DataFrame(data_frame)
#print(df)
df.to_csv('df-mundial.csv')