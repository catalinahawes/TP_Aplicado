#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 13:11:07 2026

@author: catalinahawes
"""

from Src.Principal import ruta 

def mostrar_general(archivo):
    '''
    Lee un archivo CSV y muestra toda la tabla
    
    Parametros:
        archivo: csv, con toda la informacion de la gente desaparecida
        
    Errores:
        
    Returns:
        
    '''
    
    archivo.head()
    
    
