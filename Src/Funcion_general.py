#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:11:07 2026

@author: catalinahawes
"""

def mostrar_general(archivo):
    """
    Muestra todos los casos activos registrados en el sistema.

    Recorre el DataFrame recibido y muestra la información completa de cada caso
    de forma ordenada. Si el archivo está vacío, lanza una excepción.

    Parameters
    ----------
    archivo : pandas.DataFrame
        DataFrame que contiene los casos activos. Debe incluir las columnas 
        correspondientes (N° Caso, Nombre y Apellido, etc.).

    Returns
    -------
    None
        La función no devuelve ningún valor. Muestra la información por consola.

    Raises
    ------
    ValueError
        Si el DataFrame está vacío (no hay casos activos para mostrar).
    """
    if archivo.empty:
        raise ValueError("[ERROR CRÍTICO] El archivo esta vacio")
    
   
    for indice, fila in archivo.iterrows():
        print(f"--- Fila {indice} ---")
        print(fila)
        print()
    
