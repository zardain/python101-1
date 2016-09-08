#!/usr/local/bin/python3.5
# -*- coding: utf-8 -*-
'''
@author: sergioZ

@summary: Dado un número, generar una función que indique si dicho número es primo o no lo es.
'''

def esNumeroPrimo(numero):
    if numero < 2:
        return False    
    for x in range(2, numero):
        if numero % x == 0:
            return False
    return True 
            
if __name__ == "__main__":
    numeroN = float(input("ingresar número: "))
    if esNumeroPrimo(numeroN):
        print("Es un numero primo")
    else:
        print("No es un numero primo")       
            
