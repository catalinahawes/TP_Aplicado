#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:18:50 2026

@author: catalinahawes
"""

#CODIGO PRINCIPAL
import os 
import pandas as pd

ruta= 'C:\\Users\\Sofia\\OneDrive\\Documentos\\GitHub\\TP_Aplicado\\Datos\\'
archivo= 'informacion_usuarios_argentina_unicos.csv'

df = pd.read_csv(os.path.join(ruta, archivo))


print("Opciones: 1. Mostrar general, 2. Mostrar info con filtros, 3. Agregar reporte, 4. Mostrar estadisticas, 5. Modificar estado del caso, 6. Mostrar casos ya resueltos")

opcion= int(input("Elegi una opcion: "))

while opcion != 7:
    if opcion == 1:
        general= mostrar_general(df)
    
    elif opcion == 2:
        particular= #...
     
    elif opcion == 3:
        caso_nuevo= agregar_caso()
        
    elif opcion == 4:
        estadisticas= #...
        
    elif opcion == 5:
        resuelto= #...
    
    elif opcion == 6:
        casos-resueltos= #...
        
    
    opcion= int(input("Elegi una opcion: "))
