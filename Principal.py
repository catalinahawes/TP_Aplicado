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
ruta= 'Datos'
archivo= 'informacion_usuarios_argentina_unicos.csv'

completo= os.path.join(ruta, archivo)


#ARCHIVO CASOS RESUELTOS

archivo_casos_resueltos= 'Casos resueltos.csv'

completo_2= os.path.join(ruta, archivo_casos_resueltos)


#CODIGO PRINCIPAL

opcion= 'si'
while opcion == 'si':
    print("Elija una de las siguientes opciones:")
    print("1. Mostrar general") 
    print("2. Mostrar info con filtros")
    print("3. Agregar reporte")
    print("4. Mostrar estadisticas")
    print("5. Modificar estado del caso")
    print("6. Mostrar casos ya resueltos")
    print("7. Salir")   
    
    try: 
        opcion= int(input("Elegi una opcion: "))
        
        df = pd.read_csv(completo) if os.path.exists(completo) else pd.DataFrame()
        df_2 = pd.read_csv(completo_2) if os.path.exists(completo_2) else pd.DataFrame()
         
        
        if opcion == 1:
            general= Src.Funcion_general.mostrar_general(df)
            opcion= int(input("Desea seguir?: "))
        
        elif opcion == 2:
            Src.filtrar_por_desaparecido_especifico.mostrar_caso_especifico(df)
            opcion= int(input("Desea seguir?: "))
            
        elif opcion == 3:
            caso_nuevo= Src.agregar_caso.agregar_caso(df)
            opcion= int(input("Desea seguir?: "))
            
        elif opcion == 4:
            estadisticas= Src.funcion_graficos.menu_graficos(df)
            opcion= int(input("Desea seguir?: "))
            
        elif opcion == 5:
            resuelto= Src.modificar_caso_resuelto.modificar_archivo_caso(completo, completo_2)
            opcion= int(input("Desea seguir?: "))
        
        elif opcion == 6:
            casos_resueltos= Src.mostrar_resueltos.mostrar_casos_resueltos(df_2)
            opcion= int(input("Desea seguir?: "))
       
        elif opcion == 7:
            print("¡Gracias por usar el sistema!")
            opcion= int(input("Desea seguir? si/no: "))
            break
        
        else:
            print("Opción inválida. Por favor, elegí un número del 1 al 7.")
  
    except ValueError as e:
        print(f"Error: Por favor, ingresá un número válido. ({e})")
    
    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")