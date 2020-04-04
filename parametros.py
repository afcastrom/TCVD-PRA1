#!/usr/bin/python3
# -*- coding: utf-8 -*-




import argparse

parser = argparse.ArgumentParser(description='Comparador de Precios de Vehículos')
parser.add_argument("Marca", type=str, help="Marca")
parser.add_argument("Modelo", type=str, help="Modelo")
parser.add_argument("Any_i", type=int, help="Desde Año")
parser.add_argument("Any_f", type=int, help="Hasta Año")
parser.add_argument("Ver", type=str, help="Versión")


#Contador de parametros
args = parser.parse_args()

try:
    
    marca = args.Marca
    modelo = args.Modelo
    any_i = args.Any_i
    any_f = args.Any_f
    ver = args.Ver


    
except ValueError:
    print ("Errorrrr....")



urlbase1 = "https://www.autoscout24.es/lst/%s/%s" % (marca, modelo)

# Filtros permanentes aplicados - España: cy=E, Vehículo de Ocasión: offer=U, tamaño anuncios: size=20
urlbase2 = "?sort=standard&desc=0&offer=U&ustate=N%2CU&cy=E&atype=C&size=20"

urlbase3 = "&fregto=%d&fregfrom=%d&version0=%s" % (any_f, any_i, ver)


url = urlbase1 + urlbase2 + urlbase3 + "&page=1"
print (url)

