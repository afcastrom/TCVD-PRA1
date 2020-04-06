# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:51:01 2020

@author: Julia
"""


#Analitzar el contingut en brut
from bs4 import BeautifulSoup 
import requests

#Paginación, de momento 10 (se hará parametritco)
for j in range (1,10):

    url='https://www.autoscout24.es/lst?sort=standard&desc=0&ustate=N%2CU&size=20'
    page_next=url + '&page=' + str(j)

    print (page_next)
    page=requests.get(page_next)
    

    # Comprobamos que la petición nos devuelve un Status Code = 200
    status_code = page.status_code
    
    if status_code == 200:
    
        # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
        soup = BeautifulSoup(page.content,"html.parser")
        # Obtenemos todos los divs donde están las entradas
        tags = soup.find_all('div', class_='cldt-summary-vehicle-data')
        # Obtenemos donde se encuentra el precio
        precios = soup.find_all('span', {'data-item-name': 'price'})
    
        #Por cada resultado recuperamos los datos de los coches
        for i in range(len(precios)):    
            precio=precios[i].text
            datos=tags[i].text 
  
            km=tags[i].find_all('li')[0].text
            Anyo=tags[i].find_all('li')[1].text
            KWCV=tags[i].find_all('li')[2].text
            Ocasion=tags[i].find_all('li')[3].text
            ##Propietario=tags[i].find_all('li')[4].text
            Automatico=tags[i].find_all('li')[5].text
            Combustible=tags[i].find_all('li')[6].text
            emision=tags[i].find_all('li')[8].text
        
            print(precio,km,Anyo,KWCV,Ocasion,Automatico,Combustible)
        


    else:
            
            print("error")