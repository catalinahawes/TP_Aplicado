#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:11:07 2026

@author: catalinahawes
"""
import pandas as pd

def mostrar_general(archivo):
    '''
    Lee un archivo CSV y muestra toda la tabla
    
    Parametros:
        archivo (DataFrame): datos cargados desde un CSV.
        
    Errores:
        EmptyFileError: si el archivo se encuentra vacio
        
    '''
    if archivo.empty:
        raise EmptyFileError("[ERROR CRÍTICO] El archivo esta vacio")
    
    print(archivo.head())
    