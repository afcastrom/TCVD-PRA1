#!/usr/bin/python3




import requests
from bs4 import BeautifulSoup


cn = requests.get('https://www.autoscout24.es/lst/mazda/cx-5?sort=price&desc=1&fuel=B&ustate=N%2CU&size=20&page=1&cy=E&fregto=2016&fregfrom=2014&atype=C&')

sc = cn.status_code

if sc == 200:

    # Pasamos el contenido HTML de la web a un objeto BeautifulSoup()
    html = BeautifulSoup(cn.text, "html.parser")

    # Obtenemos todos los divs donde están las entradas
    entradas = html.findAll("data-item-name", {"class": "listing-summary-container"})

    # Recorremos todas las entradas para extraer el título, autor y fecha
    for i, entrada in enumerate(entradas):
        # Con el método "getText()" no nos devuelve el HTML
  
        version = entrada.find('h2', {'class': 'cldt-summary-version sc-ellipsis'}).getText()
        precio = entrada.find('span', {'data-item-name': 'price'}).getText()
        

        # Imprimo el Título, Autor y Fecha de las entradas
        print (version, precio)
else:
    print ("Status Code" % sc)


# Saving the scraped text
#with open('scraped_text.txt', 'w') as file:
#    file.write(article)

    
