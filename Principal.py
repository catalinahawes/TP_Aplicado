#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:18:50 2026

@author: catalinahawes
"""


import os 
import pandas as pd

#IMPORT DE LAS FUNCIONES
import Src.Funcion_general
import Src.modificar_caso_resuelto
import Src.agregar_caso
import Src.funcion_graficos
import Src.mostrar_resueltos
import Src.filtrar_por_desaparecido_especifico

#ARCHIVO CON INFO
ruta= 'Datos\\'
archivo= 'informacion_usuarios_argentina_unicos.csv'

completo= ruta + archivo

df = pd.read_csv(os.path.join(ruta, archivo))

#ARCHIVO CASOS RESUELTOS
ruta_2= "Datos\\"
archivo_casos_resueltos= 'Casos resueltos.csv'

completo_2= ruta_2 + archivo_casos_resueltos

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
    try: 
        if opcion == 1:
            general= Src.Funcion_general.mostrar_general(df)
        
        elif opcion == 2:
            nombre= Src.filtrar_por_desaparecido_especifico.mostrar_caso_especifico(df)    
             
            particular= Src.filtrar_por_desaparecido_especifico.filtrar_participante(df, nombre)
            
        elif opcion == 3:
            caso_nuevo= Src.agregar_caso.agregar_caso(df)
            
        elif opcion == 4:
            estadisticas= Src.funcion_graficos.menu_graficos(df)
            
        elif opcion == 5:
            resuelto= Src.modificar_caso_resuelto.modificar_archivo_caso(completo, completo_2)
        
        elif opcion == 6:
            casos_resueltos= Src.mostrar_resueltos.mostrar_casos_resueltos(df_2)
        
    except ValueError as e:
        print(e)
    
    
    finally: 
        opcion= int(input("Elegi una opcion: "))

