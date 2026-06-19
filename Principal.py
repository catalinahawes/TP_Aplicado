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
    """
    Carga el archivo Excel que contiene los casos activos.

    Intenta leer el archivo ubicado en la ruta definida. Si el archivo no existe,
    lanza una excepción clara indicando que debe crearse o verificarse la ruta.
    Cualquier otro error durante la lectura también es propagado.

    Returns
    -------
    pandas.DataFrame
        DataFrame con los casos activos cargados desde el archivo Excel.

    Raises
    ------
    FileNotFoundError
        Si el archivo de casos activos no se encuentra en la ruta especificada.
    Exception
        Para cualquier otro error ocurrido durante la lectura del archivo.
    """
    
    try:
        df_activos = pd.read_excel(ruta_activos, header=0)
        return df_activos
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encontró el archivo de casos activos: {ruta_activos}. Creá el archivo o verificá la ruta antes de ejecutar.")
        
    except Exception as e:
        raise Exception(f"Error al leer el archivo de casos activos: {e}")
    
def cargar_resueltos():
    """
    Carga el archivo Excel que contiene los casos ya resueltos.

    Si el archivo no existe, muestra un mensaje informativo y devuelve un 
    DataFrame vacío (para que el programa pueda seguir funcionando y crear 
    el archivo cuando se marque el primer caso como resuelto).

    Returns
    -------
    pandas.DataFrame
        DataFrame con los casos resueltos. Si el archivo no existe, 
        se devuelve un DataFrame vacío.

    Raises
    ------
    Exception
        Si ocurre un error distinto a que el archivo no exista.
    """
    try:
        df_resueltos = pd.read_excel(ruta_resueltos, header=0)
        return df_resueltos
    except FileNotFoundError:
        print("Archivo de casos resueltos no encontrado. Se creará uno nuevo cuando marques un caso como resuelto.")
        return pd.DataFrame()
    except Exception as e:
        raise Exception(f"Error al leer el archivo de casos resueltos: {e}")

   

def mostrar_menu():
    """
    Muestra el menú principal de opciones del sistema.

    Imprime en pantalla las 7 opciones disponibles para que el usuario 
    pueda seleccionar qué acción desea realizar.

    Returns
    -------
    None
        La función solo imprime información por consola.
    """
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
    """
    Función principal del programa.

    Coordina todo el flujo del sistema de gestión de casos de desaparecidos.
    Carga los archivos de casos activos y resueltos, muestra el menú al usuario,
    ejecuta la opción seleccionada y maneja el flujo de continuar o salir del programa.

    Esta función actúa como el punto de entrada principal de la aplicación.

    Returns
    -------
    None
        La función gestiona todo el ciclo de vida del programa hasta que el usuario decide salir.
    """
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
            
            if seguir in ['si', 's', 'yes', 'y']:
                break
            elif seguir in ['no', 'n']:
                print("¡Gracias por usar el sistema!")
                return
            else:
                print("Respuesta inválida. Escribí 'si' o 'no'.")
                
main()











