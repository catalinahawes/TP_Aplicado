#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:18:50 2026

@author: catalinahawes
"""


import os 
import pandas as pd

#IMPORT DE LAS FUNCIONES
import Funcion_general
import modificar_caso_resuelto
import agregar_caso
import funcion_graficos
import mostrar_resueltos
import filtrar_por_desaparecido_especifico

#ARCHIVO CON INFO
ruta= 'C:\\Users\\Sofia\\OneDrive\\Documentos\\GitHub\\TP_Aplicado\\Datos\\'
archivo= 'informacion_usuarios_argentina_unicos.csv'

df = pd.read_csv(os.path.join(ruta, archivo))

#ARCHIVO CASOS RESUELTOS
ruta_2= "C:\\Users\\Sofia\\OneDrive\\Documentos\\GitHub\\TP_Aplicado\\Datos\\"
archivo_casos_resueltos= 'Casos resueltos.csv'

df_2 = pd.read_csv(os.path.join(ruta_2, archivo_casos_resueltos))


#CODIGO PRINCIPAL
print("Elija una de las siguientes opciones:")
print("1. Mostrar general") 
print("2. Mostrar info con filtros")
print("3. Agregar reporte")
print("4. Mostrar estadisticas")
print("5. Modificar estado del caso")
print("6. Mostrar casos ya resueltos")
print("7. Salir")

opcion= int(input("Elegi una opcion: "))

while opcion != 7:
    if opcion == 1:
        general= Funcion_general.mostrar_general(df)
    
    elif opcion == 2:
        particular= filtrar_por_desaparecido_especifico.filtrar_participante(df)
     
    elif opcion == 3:
        caso_nuevo= agregar_caso.agregar_caso(df)
        
    elif opcion == 4:
        estadisticas= funcion_graficos.menu_graficos(df)
        
    elif opcion == 5:
        resuelto= modificar_caso_resuelto.modificar_archivo_caso(df, df_2)
    
    elif opcion == 6:
        casos_resueltos= mostrar_resueltos.mostrar_casos_resueltos(df_2)
        
    
    opcion= int(input("Elegi una opcion: "))
