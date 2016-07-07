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
def open_csv():
    try:
        file_name = input("Nome do arquivo:")
        csv_file = open(file_name + ".csv",'r',errors='ignore', encoding ="UTF-8")
        return [csv_file,file_name] 
    except:
        print("Arquivo inexistente.\n")
        return open_csv()

####################################################
# Main
####################################################
Registers = []
files = []

k = open_csv()

f = k[0]

handler = k[1]

del k 
# processamento de arquivo 
offset = 0

if os.path.isfile(handler + 'Data.bin') == False:
    with open(handler + 'Data.bin', "wb") as handler_data:
        for line in csv.reader(f, dialect= 'excel',delimiter=''):
            if line[0] == "Videotitle link_link":
                del line 
            else:
                i = 1
                for element in line[1]:
                    i = i + 1
                    if element =="":
                        del line[i-1::]
                newElement = Register(offset,line)
                Registers.append(newElement)
                pickle.dump(newElement, handler_data, pickle.HIGHEST_PROTOCOL)

                offset = offset + 1
    f.close()

    make_index_files(Registers, handler)

print("\nArquivo " + handler + " aberto e processado com sucesso\n")

arquivo_de_saida = input("Para melhor visualizacao de dados, um arquivo txt sera criado. Digite o nome dele: ")
arquivo_de_saida = arquivo_de_saida + ".txt"
print(arquivo_de_saida + "criado\n")
saida = open(arquivo_de_saida,"w")

menu = 1
while menu != 99:
    print("""_____ ______ ________ _________ ___ ___ ________ _______ ________ ________ ________ ___ ___
|\ _ \ _ \|\ __ \|\___ ___\\ \|\ \ |\ ____\|\ ___ \ |\ __ \|\ __ \|\ ____\|\ \|\ \
\ \ \\\__\ \ \ \ \|\ \|___ \ \_\ \ \\\ \ \ \ \___|\ \ __/|\ \ \|\ \ \ \|\ \ \ \___|\ \ \\\ \
\ \ \\|__| \ \ \ __ \ \ \ \ \ \ __ \ \ \_____ \ \ \_|/_\ \ __ \ \ _ _\ \ \ \ \ __ \
\ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \ \|____|\ \ \ \_|\ \ \ \ \ \ \ \\ \\ \ \____\ \ \ \ \
\ \__\ \ \__\ \__\ \__\ \ \__\ \ \__\ \__\ ____\_\ \ \_______\ \__\ \__\ \__\\ _\\ \_______\ \__\ \__\
\|__| \|__|\|__|\|__| \|__| \|__|\|__| |\_________\|_______|\|__|\|__|\|__|\|__|\|_______|\|__|\|__|
\|______|""")
    print ("Bem-vindo ao MATH_SEARCH\n")
    print ("[1] - Listagem de todos videos\n")
    print ("[2] - Busca por palavra-chave\n")
    print ("[99] - Saida do programa\n")
    menu=int(input())
    switch(menu,handler,saida)
    input()