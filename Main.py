"""
Proyecto Algoritmos y Programación "Metrotify"
Autor: Michelle García
"""

from Program import Program
import os
os.system('cls')


"""----------------------------------- Función principal de Metrotify ----------------------------------"""

def main():

    Metrotify = Program()
    Metrotify.download()
    Metrotify.open_database()
    Metrotify.menu()

main ()
