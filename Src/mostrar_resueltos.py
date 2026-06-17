#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:24:17 2026

@author: catalinahawes
"""

def mostrar_casos_resueltos(archivo_2):
    '''
    Lee un archivo CSV de los casos ya resuektos y muestra toda la tabla
    
    Parametros:
        archivo_2 (DataFrame): datos cargados desde un CSV.
        
    Errores:
        ValueError: si el archivo se encuentra vacio
        
    '''
    if archivo_2.empty:
        raise ValueError("[ERROR CRÍTICO] El archivo esta vacio")
    
   
    for indice, fila in archivo_2.iterrows():
        print(f"--- Fila {indice} ---")
        print(fila)
        print()
    
