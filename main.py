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


def video_name(name_archive, word, exit):
    # Busca palvra consultada
    # Imprime todos videos com a palavra consultada
    list_vid = []

    f = open(name_archive + "data_word_index.bin",'rb')

    tree = pickle.load(f)

    word = word.lower()

    list_vid = list_video(word,tree,name_archive)

    print_list(list_vid)

    if list_vid != None:
        for i in list_vid:
            r = i.__repr__()
            exit.write(r + "\n\n")

    f.close()

#####################################################
def verify_entry(nomedaentrada):
    try:
        entrada = open(nomedaentrada+"data_name_videos_index.bin",'wb')
        print("\nArquivo ja processado anteriormente\n")
        entrada.close()
        return True
    except:
        print("\nArquivo novo.\nVamos processar o arquivo pela primeira vez.\nAguarde\n")
        return False
#####################################################
def test():
    try:
        handler = input("Nome do arquivo:")
        f = open(handler + ".csv",'r',errors='ignore', encoding ="UTF-8")
        return [f,handler]
    except:
        print("Arquivo inexistente.\n")
        return test()

####################################################
# Main
####################################################
Registers = []
files = []

k = test()

f = k[0]

handler = k[1]

del k 
# processamento de arquivo 
offset = 0