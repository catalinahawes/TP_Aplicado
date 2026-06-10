# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 08:36:08 2026

@author: mimib
"""

import pandas as pd
   #fijarme como llamo a esos parametros en el main 
def modificar_archivo_caso(archivo_activos,archivo_resueltos):
    """
    Busca una denuncia activa en el programa principal. 
    SI encuentra el caso lo elimina del archivo denuncias ylo agrega 
    al archivo de denuncias resueltas, donde estan los casos ya encontrados. 
    La función valida los datos ingresados por el usuario y muestra mensajes de error
    si algún dato está vacío, tiene formato incorrecto o no se encuentra el caso.
    Parameters
    ----------
    archivo_activos: str
        informacion_usuarios_argentina_unicos.csv
    archivo_resueltos: str
       Casos resueltos.csv
    Returns:
        La funcion no devuelve ningun valor, modifica los archivos de excel y muestra mensajes por consola
   
    """
    try:
        df=pd.read_excel(archivo_activos,header= 2)
        #crea data frame 
        #read_Excel= Leé el archivo Excel llamado archivo_activos, usá la fila número 2 como encabezado de columnas, y guardá esa tabla en df
        if len(df)== 0:
            raise ValueError("El archivo de casos esta vacio")
        
        print("Ingrese los datos del caso que desea marcar como resuelto")
        #ver de poner todo esto en una funcion de validar
        nombre= input("Ingrese nombre y apellido: ")
        if nombre== "":
            raise ValueError("El nombre y apellido no puede estar vacio")
        if nombre != nombre.title():
            raise ValueError ("El nombre y apellido debe escribirse en mayuscula inicial, Ejemplo: Juan Perez")
        edad= input("Edad:")    
        if edad== "":
            raise ValueError("La edad no puede estar vacia")
        edad= int(edad)
        if edad <= 0:
            raise ValueError("La edad no puede ser negativa")
        genero= input("Genero:")
        if genero == "":
            raise ValueError("El genero no puede estar vacio")
        peso= input("Peso en Kg:")
        if peso == "":
            raise ValueError("El peso no puede estar vacio")
        peso= float(peso)
        if peso <= 0: 
            raise ValueError("El peso no puede ser negativo")
        altura= input("Ingrese altura")
        if altura =="":
            raise ValueError("Los datos no pueden estar vacios")
        altura= float(altura)
        if altura<=0:
            raise ValueError("La altura debe ser mayor a 0")
        rasgos_fisicos= input("Rasgos fisicos:")
        if rasgos_fisicos == "":
            raise ValueError("Los rasgos no pueden estar vacios")
        zona= input("Ingrese zona: ")
        if zona == "":
                raise ValueError("La zona no puede estar vacía.")
        datos_extra= input("Datos extra: ")
        if datos_extra == "":
            raise ValueError("Los datos no pueden estar vacios")
        
        caso = df[
                (df["Nombre y Apellido"] == nombre) &
                (df["Edad"] == edad) &
                (df["Género"] == genero) &
                (df["Peso (kg)"] == peso) &
                (df["Altura (m)"] == altura) &
                (df["Rasgos Físicos"] == rasgos_fisicos) &
                (df["Zona (Argentina)"] == zona) &
                (df["Datos Extra"] == datos_extra)
            ]
        if len(caso)== 0:
            raise ValueError("No se encontro una denuncia con esos datos")
        indice= caso.index[0]
        dfsincaso= df.drop(indice) 
        
        df_excel_resueltos= pd.read_excel(archivo_resueltos) #ver como se llama la variable de verdad
        df_excel_resueltos=  pd.concat([df_excel_resueltos, caso], ignore_index=True)
        
        dfsincaso.to_excel(archivo_activos, index=False, startrow=2)
        df_excel_resueltos.to_excel(archivo_resueltos, index=False)
        
        print("El caso fue marcado como resuelto correctamente")
        print("se elimino del archivo de casos activos")
        print(" se agrego el archivo de casos resueltos")
    except FileNotFoundError: 
        print("Error: No se encontro ninguno")
    
    except ValueError as error:
        print("Error", error)
    except PermissionError:
        print("Error, no se pudo guardar el archivo")
    except KeyError: 
        print("Error, alguna columna no existe o esta escrita distinta en el archivo")
    except Exception as error:
        print("Ocurrio un error inesperado.")
        print(error)
        
    
