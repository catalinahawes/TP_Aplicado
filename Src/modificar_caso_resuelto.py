# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:36:08 2026

@author: mimib
"""
import os
import pandas as pd
from Src.funcion_validacion import validar_entero_positivo


def modificar_archivo_caso(archivo_activos, archivo_resueltos):
    """
    Permite marcar uno o varios casos como resueltos de forma consecutiva.
    
    Busca un caso activo por su número, lo elimina del archivo de casos activos
    y lo agrega al archivo de casos resueltos. Al finalizar, pregunta al usuario
    si desea seguir modificando más casos.

    Parameters
    ----------
    archivo_activos : str
        Ruta del archivo Excel que contiene los casos activos.
    archivo_resueltos : str
        Ruta del archivo Excel que contiene los casos ya resueltos.

    Returns
    -------
    None
        La función no devuelve ningún valor. Modifica ambos archivos Excel
        y muestra mensajes informativos por consola.
    """

    while True:   
        try:
            df = pd.read_excel(archivo_activos, header=0)

            if len(df) == 0:
                print("El archivo de casos activos está vacío.")
                return

            if "N° Caso" not in df.columns:
                print("No existe la columna 'N° Caso' en el archivo.")
                return

            print("\nIngrese el número del caso que desea marcar como resuelto.")
            numero_caso = input("Número de caso: ")
            numero_caso = validar_entero_positivo(numero_caso, "número de caso")

            caso = df[df["N° Caso"] == numero_caso]

            if len(caso) == 0:
                print("No se encontró un caso con ese número de caso.")
                continue

           
            df_sin_caso = df.drop(caso.index[0])

            
            if os.path.exists(archivo_resueltos):
                df_resueltos = pd.read_excel(archivo_resueltos, header=0)
            else:
                df_resueltos = pd.DataFrame(columns=df.columns)

            df_resueltos = pd.concat([df_resueltos, caso], ignore_index=True)

            
            df_sin_caso.to_excel(archivo_activos, index=False)
            df_resueltos.to_excel(archivo_resueltos, index=False)

            print("El caso fue marcado como resuelto correctamente.")
            print("Se eliminó del archivo de casos activos.")
            print("Se agregó al archivo de casos resueltos.")

        except FileNotFoundError:
            print("Error: No se encontró alguno de los archivos.")
            return
        except PermissionError:
            print("Error: No se pudo guardar el archivo. Cerralo si está abierto en Excel.")
            return
        except Exception as error:
            print("Ocurrió un error inesperado:", error)
            return

        
        while True:
            continuar = input("\n¿Desea seguir modificando más casos? (si/no): ").strip().lower()
            
            if continuar in ['si', 's', 'yes', 'y']:
                break          
            elif continuar in ['no', 'n']:
                print("Volviendo al menú principal...")
                return         
            else:
                print("Por favor, responda 'si' o 'no'.")