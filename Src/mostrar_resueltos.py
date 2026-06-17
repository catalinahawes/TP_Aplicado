#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 15:24:17 2026

@author: catalinahawes
"""
import pandas as pd

from IPython.display import display

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
    
    #print(archivo_2.head())
    
    with pd.option_context('display.max_rows', None, 'display.max_columns', None):
        display(archivo_2)