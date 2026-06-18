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


ruta_datos = 'Datos'
archivo_activos = "informacion_usuarios.xlsx"
archivo_resueltos = 'Casos resueltos.xlsx'

ruta_activos = os.path.join(ruta_datos, archivo_activos)
ruta_resueltos = os.path.join(ruta_datos, archivo_resueltos)

def cargar_activos():
    """Carga los archivos Excel de casos activos"""
    
    try:
        df_activos = pd.read_excel(ruta_activos, header=0)
        print("Casos activos cargados correctamente")
        return df_activos
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo de casos activos: {ruta_activos}. Creá el archivo o verificá la ruta antes de ejecutar.")
        
    except Exception as e:
        raise Exception(f"Error al leer el archivo de casos activos: {e}")
    
def cargar_resueltos():
    try:
        df_resueltos = pd.read_excel(ruta_resueltos, header=0)
        print("Casos resueltos cargados correctamente")
        return df_resueltos
    except FileNotFoundError:
        print("Archivo de casos resueltos no encontrado. Se creará uno nuevo cuando marques un caso como resuelto.")
        return pd.DataFrame()
    except Exception as e:
        raise Exception(f"Error al leer el archivo de casos resueltos: {e}")

   

def mostrar_menu():
    print("Elija una de las siguientes opciones:")
    print("="*55)
    print("1. Mostrar general (todos los casos activos)")
    print("2. Mostrar info con filtros (caso específico)")
    print("3. Agregar reporte")
    print("4. Mostrar estadísticas (gráficos)")
    print("5. Modificar estado del caso (marcar como resuelto)")
    print("6. Mostrar casos ya resueltos")
    print("7. Salir")
    print("="*55)

def main():
    df_activos = cargar_activos()
    df_resueltos = cargar_resueltos()
    while True:
        mostrar_menu()
        try:
            opcion = int(input("Elegí una opción (1-7): "))
            
            if opcion == 1:
                mostrar_general(df_activos)
                
            elif opcion == 2:
                mostrar_caso_especifico(df_activos)
                
            elif opcion == 3:
                agregar_caso(ruta_activos)
                df_activos = cargar_activos()           
                
            elif opcion == 4:
                menu_graficos(df_activos)
                
            elif opcion == 5:
                modificar_archivo_caso(ruta_activos, ruta_resueltos)
                df_activos = cargar_activos()           
                df_resueltos = cargar_resueltos()      
                
            elif opcion == 6:
                mostrar_casos_resueltos(df_resueltos)
                
            elif opcion == 7:
                print("¡Gracias por usar el sistema! Hasta pronto.")
                break
                
            else:
                print("Opción inválida. Por favor, elegí un número del 1 al 7.")
                continue
            
                    
        except ValueError as e:
            if "invalid literal for int()" in str(e):
                print("Error: Por favor, ingresá un número válido.")
            else:
                print(f"Error: {e}")
    
        except Exception as e:
            print(f"Ocurrió un error inesperado: {e}")
            
        while True:
            seguir = input("¿Querés hacer otra acción? (si/no): ").strip().lower()
            
            if seguir in 'si':
                break
            elif seguir in 'no':
                print("¡Gracias por usar el sistema!")
                return
            else:
                print("Respuesta inválida. Escribí 'si' o 'no'.")
                
main()











