# -*- coding: utf-8 -*-
"""
Created on Wed Jun 10 10:12:13 2026

@author: mimib
"""

def validar_texto_obligatorio(dato,nombre_campo):
    """
    Valida que un dato de texto no esté vacío.

    Parameters
    ----------
    dato : str
        Texto ingresado por el usuario.

    nombre_campo : str
        Nombre del campo que se está validando.Ejemplo: nombre, genero

    Returns
    -------
    str
        Devuelve el texto ingresado si es válido.

    Raises
    ------
    ValueError
        Si el dato está vacío.
    """
    if dato== "":
        raise ValueError( f"el campo {nombre_campo} no puede estar vacio")
    return dato 

def validar_nombre_apellido(nombre):
    """
    Valida que el nombre y apellido no esten vacios y que esten escritos
    con mayuscula inicial.

    Parameters
    ----------
    nombre : str
        Nombre y apellido ingresado por el usuario.

    Returns
    -------
    str
        Devuelve el nombre si es válido.

    Raises
    ------
    ValueError
        Si el nombre está vacío o no tiene mayúscula inicial.
    """    
    if nombre== "":
        raise ValueError("El nombre y apellido no puede estar vacio.")
    if nombre != nombre.title():
        raise ValueError("El nombre y apellido debe escribirse con mayuscula incicial.")
    return nombre
def validar_entero_positivo(dato,nombre_campo):
    """
   valida que un dato sea un numero entero mayor a 0.

   Parameters
   ----------
   dato : str
       Dato ingresado por el usuario.

   nombre_campo : str
       Nombre del campo que se está validando.Ej: Peso,altura,edad

   Returns
   -------
   int
       Devuelve el dato convertido a numero entero.

   Raises
   ------
   ValueError
       Si el dato está vacío, no es un entero o es menor o igual a 0.
   """
    if dato== "":
       raise ValueError( f"el campo {nombre_campo} no puede estar vacio")
    dato= int(dato)
    if dato<= 0:
        raise ValueError(f"El campo {nombre_campo} debe ser mayor a cero ")
    return dato
def valida_decimal_positivo(dato,nombre_campo):
    """
    Valida que un dato sea un número decimal mayor a 0.

    Parameters
    ----------
    dato : str
        Dato ingresado por el usuario.

    nombre_campo : str
        Nombre del campo que se está validando.

    Returns
    -------
    float
        Devuelve el dato convertido a número decimal.

    Raises
    ------
    ValueError
        Si el dato está vacío, no es un número o es menor o igual a 0.
    """

    if dato== "":
        raise ValueError( f"el campo {nombre_campo} no puede estar vacio")
    dato= float(dato)
    if dato<= 0:
         raise ValueError(f"El campo {nombre_campo} debe ser mayor a cero ")
    return dato