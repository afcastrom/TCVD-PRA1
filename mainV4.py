# -*- coding: utf-8 -*-
"""
Created on Tue Mar 31 17:51:01 2020

@author: Julia & Toni
"""
import os
import csv
import argparse
from bs4 import BeautifulSoup 
import requests
import sys
from datetime import datetime

parser = argparse.ArgumentParser(description='Precios Venta Vehículos Particulares')
parser.add_argument("Marca", help="Marca (obligatorio)")
parser.add_argument("Modelo", help="Modelo (obligatorio)")
parser.add_argument("Any_i", nargs="?", default='0', type=int, help="Desde Año")
parser.add_argument("Any_f", nargs="?", default='0', type=int, help="Hasta Año")
parser.add_argument("Ver", nargs="?", default='', help="Versión")

#Fecha de ejecución
now = datetime.now()
fecha = now.strftime('%d/%m/%Y')


args = parser.parse_args()
marca = args.Marca
modelo = args.Modelo
any_i = args.Any_i
any_f = args.Any_f
ver = args.Ver

 
# Filtros permanentes aplicados:
# España: cy=E, Vehículo de Ocasión: offer=U, tamaño anuncios: size=20, page=1

# Filtros obligatorios/opcionales pasados como parámetros:
# /MARCA/MODELO/, fregto=DESDE AÑO, fregfrom=HASTA AÑO, version0=VERSION, custtype=PARTICULAR/PROFESIONAL (vacio: ambos)


url =  "https://www.autoscout24.es/lst/%s/%s?sort=standard&desc=0&custtype=P&offer=U&ustate=N" % (marca, modelo) + "%2CU" + "&cy=E&atype=C&size=20&fregto=%d&fregfrom=%d&version0=%s" % (any_f, any_i, ver) 



def encontrarCoches(url):
    #Paginación, de momento 10 (se hará parametritco)




    for j in range (1,10):
        
        page_next=url + '&page=' + str(j)
      
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
            # Obtenemos los datos de modelo y version
            t2 = soup.find_all('div', class_='cldt-summary-title')
            # Obtenemos los datos de la ciudad, en función del tipo de vendedor
            par = soup.find_all('span', class_='cldt-summary-seller-contact-zip-city') # particular                       
            #pro = soup.find_all('span', class_='cldf-summary-seller-contact-zip-city') # profesional                      

            #Por cada resultado recuperamos los datos de los coches
            for i in range(len(precios)):  
                precio=precios[i].text.replace("IVA deducible", '').replace("€", '').replace(",-", '').replace(".", '') #precio
                #controlamos si tiene versión o no (no todos tienen)
                filas=t2[i].find_all('h2')
                #controlamos el tipo de vendedor

                              
                
                mod=t2[i].find_all('h2')[0].text #modelo
                km=tags[i].find_all('li')[0].text.replace("km", '') #kilometraje
                Anyo=tags[i].find_all('li')[1].text #Anyo
                KWCV=tags[i].find_all('li')[2].text #Cilindrada
                Automatico=tags[i].find_all('li')[5].text #Automatico
                Elec=tags[i].find_all('li')[6].text # Electrico
                ciudad=par[i].text # ciudad            
                
                #Guardamos los datos
                if (len(filas))==2:
                   ver=t2[i].find_all('h2')[1].text #versión
                   DatosCoches=[fecha,mod,ver,precio,km,Anyo,KWCV,Automatico,Elec,ciudad]
                else:
                   DatosCoches=[fecha,mod,"n/a",precio,km,Anyo,KWCV,Automatico,Elec,ciudad]

                                             
                #Primero eliminamos saltos de lineas
                DatosCochesF=[]
                for elemento in DatosCoches:
                    elementoF=elemento.strip() #strip elimina espacios en blanco
                    DatosCochesF.append(elementoF)
                
                ListaCoches.append(DatosCochesF)

        else:                
            print("Error en acceso a la página")
                
            
    return

ListaCoches=[]
Cabecera=["Fecha","Modelo","Versión","Precio","Kilometraje","Año","Motor","Tipo","Ciudad"]
ListaCoches.append(Cabecera)
#Directorio del script
Directorio = os.path.dirname(__file__)
print(Directorio)
Fichero = "Datos_coches_ventas.csv"
FicheroPath = os.path.join(Directorio, Fichero)

#Llamada a la funcion
encontrarCoches(url)

#Escribimos en el fichero los datos


with open(FicheroPath, 'w', newline='') as csvFile:
  writer = csv.writer(csvFile)
  for DatosCoches in ListaCoches:
    writer.writerow(DatosCoches)
