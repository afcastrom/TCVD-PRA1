# CochesVentaScrap

## Descripcion script

Permite extraer la información de coches de particulares en venta, en una web de segunda mano , con el fin de poder aportar información a un posible vendedor. 

Los paramétros de entrada serán los siguientes:

1. Marca: Marca del coche a buscar (Obligatorio)
2. Modelo: Modelo del coche a buscar (Obligatorio)
3. Año inicio y fin: Rangos de fecha del coche a buscar (Opcional)
4. Versión: Versión del coche a buscar (Opcional)

## Bibliotecas necesarias para ejecutar el script

El desarrollo del script se ha realizado en phyton y se necesita instalar las bibliotecas siguientes:

    import os
    import csv
    import argparse
    from bs4 import BeautifulSoup
    import requests
    import sys
    from datetime import datetime

## Ejecución

La ejecución del script se realizará de la siguiente forma:

    python foodPriceScraper.py Marca Modelo inicio fin version
    
Se muestra une ejemplo de llamada, informando los datos obligatorios:

    python foodpricescraper.py BMW i3
    python foodpricescraper.py AUDI A3 2015 2015
    
    
## Extración a fichero

Se genera un fichero de salida en formato .csv con los siguientes datos:
    Fecha
    Modelo
    Versión
    Precio
    Kilometraje
    Mes/Año
    Potencia
    Cambio
    Combustible
    Ciudad
   
## Integrantes   
   La práctica ha sido realizada por Julia Soler (jsolerni@uoc.edu)  & Antonio Castro (acastrom@uoc.edu).
   
