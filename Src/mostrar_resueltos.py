#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:24:17 2026

@author: catalinahawes
"""

def mostrar_casos_resueltos(archivo_2):
    """
    Muestra todos los casos que ya fueron marcados como resueltos.

    Recorre el DataFrame de casos resueltos y muestra la información completa 
    de cada caso de forma ordenada. Si no hay casos resueltos, informa al usuario 
    y finaliza la ejecución de la función sin generar errores.

    Parameters
    ----------
    archivo_2 : pandas.DataFrame
        DataFrame que contiene los casos ya resueltos. Debe tener las mismas 
        columnas que el archivo de casos activos.

    Returns
    -------
    None
        La función no devuelve ningún valor. Muestra la información por consola.
    """
    if archivo_2.empty:
        print("No hay casos resueltos todavía.")  
        return
   
    for indice, fila in archivo_2.iterrows():
        print(f"--- Fila {indice} ---")
        print(fila)
        print()
    
