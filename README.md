# Descripción script CochesVentaScrap

Permite extraer la información de coches en venta de una web de segunda mano, con el fin de poder aportar información a un posible vendedor. 
Los paramétros de entrada serán los siguientes:

1. Marca: Marca del coche a buscar (Obligatorio)
2. Modelo: Modelo del coche a buscar (Obligatorio)
3. Año inicio y fin: Rangos de fecha del coche a buscar (Opcional)
4. Versión: Versión del coche a buscar (Opcional)

## Bibliotecas necesarias para ejecutar el script

Se necesita instalar las bibliotecas siguientes:

import os

import csv

import argparse

from bs4 import BeautifulSoup 
import requests
import sys
from datetime import datetime
