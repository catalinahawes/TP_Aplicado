#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  4 14:18:50 2026

@author: catalinahawes
"""


import os
import pandas as pd


from Src.Funcion_general import mostrar_general
from Src.modificar_caso_resuelto import modificar_archivo_caso
from Src.agregar_caso import agregar_caso
from Src.funcion_graficos import menu_graficos
from Src.mostrar_resueltos import mostrar_casos_resueltos
from Src.filtrar_por_desaparecido_especifico import mostrar_caso_especifico


ruta = 'Datos'
archivo_activos = 'informacion_usuarios_argentina_unicos.xlsx'
archivo_resueltos = 'Casos resueltos.xlsx'

completo_activos = os.path.join(ruta, archivo_activos)
completo_resueltos = os.path.join(ruta, archivo_resueltos)


try:
    df = pd.read_csv(completo_activos, encoding='latin1')
except:
    df = pd.DataFrame()

try:
    df_resueltos = pd.read_csv(completo_resueltos, encoding='latin1')
except:
    df_resueltos = pd.DataFrame()




while True:
    
    print("Elija una de las siguientes opciones:")
    print("1. Mostrar general (todos los casos activos)")
    print("2. Mostrar info con filtros (caso específico)")
    print("3. Agregar reporte")
    print("4. Mostrar estadísticas (gráficos)")
    print("5. Modificar estado del caso (marcar como resuelto)")
    print("6. Mostrar casos ya resueltos")
    print("7. Salir")
    
    try:
        opcion = int(input("Elegí una opción (1-7): "))
        
        if opcion == 1:
            print("Mostrando todos los casos activos")
            mostrar_general(df)
            
        elif opcion == 2:
            print("Buscar caso específico")
            mostrar_caso_especifico(df)
            
        elif opcion == 3:
            print("Agregar nuevo caso")
            agregar_caso(completo_activos)
            # Recargamos después de agregar
            try:
                df = pd.read_csv(completo_activos, encoding='latin1')
            except:
                df = pd.DataFrame()
            
        elif opcion == 4:
            print("Estadísticas y Gráficos")
            menu_graficos(df)
            
        elif opcion == 5:
            print("Marcar caso como resuelto")
            modificar_archivo_caso(completo_activos, completo_resueltos)
            try:
                df = pd.read_csv(completo_activos, encoding='latin1')
            except:
                df = pd.DataFrame()
            try:
                df_resueltos = pd.read_csv(completo_resueltos, encoding='latin1')
            except:
                df_resueltos = pd.DataFrame()
            
        elif opcion == 6:
            print("Mostrando casos ya resueltos")
            mostrar_casos_resueltos(df_resueltos)
            
        elif opcion == 7:
            print("¡Gracias por usar el sistema! Hasta pronto.")
            break
            
        else:
            print("Opción inválida. Por favor, elegí un número del 1 al 7.")
            continue
        
        # Preguntar si quiere seguir
        while True:
            seguir = input("¿Desea realizar otra acción? (si/no): ").strip().lower()
            if seguir in ['si', 's', 'yes', 'y']:
                break
            elif seguir in ['no', 'n']:
                print("¡Gracias por usar el sistema!")
                exit()
            else:
                print("Por favor, responda 'si' o 'no'.")
                
    except ValueError as e:
        if "invalid literal for int()" in str(e):
            print("Error: Por favor, ingresá un número válido.")
        else:
            print(f"Error: {e}")

    except Exception as e:
        print(f"Ocurrió un error inesperado: {e}")