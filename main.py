#   Arquivo principal do trabalho final de CPD
#   E: Arquivo de texto com links do youtube 
#   S: Arquivos binario com dados e um arquivo de texto 

import os
from CSV_ import *
#===============================
#   functions
#===============================


def switch(menu, handler,exit):
    while menu != 99:
        if menu == 1:
            print("Listagem de videos.\n")
            exit.write("Listagem de videos.\n")

            video(handler,exit)
            break
        elif menu == 2:
            print ("Busca por palavras chaves.\n")
            exit.write("Busca por palavras chaves.\n")

            videos(handler,input("Digite: "), exit)
            break
        else:
            print ("Valor invalido, tente novamente\n")
            return 0
    if menu == 99:
        print("Fim\n")
        exit.write("Arquivo Fechado.\n")
        exit.close()
        
    return 0
#####################################################