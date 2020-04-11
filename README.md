# CochesVentaScrap

## Descripcion script

Permite extraer la información de coches en venta de una web de segunda mano, con el fin de poder aportar información a un posible vendedor. 
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

    python foodPriceScraper.py Mara Modelo inicio fin version
    
Se muestra une ejemplo de llamada, informando los datos obligatorios:

    python foodPriceScraper.py BMW i3
    
## Extración a fichero

Se genera un fichero de salida en formato .csv con los siguientes datos:

   Modelo: Modelo del coche
   Versión: Versión del coche
   Precio: Precio del coche
   Kilometraje: Km del coche
   Año: Año del coche
   Motor: Cilindrada
   Tipo: Electrico, gasolina
   
   
   
