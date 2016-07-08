#!/usr/bin/env python3
import csv
import re 
import hashlib
import pickle

###################
"""
Arvore Trie => pode ser convertida em patricia

onde:

value -> parte do codigo que o nodo representa
children_l -> filho esquerdo do nodo
children_r -> filho direito do nodo 
offset -> offset em outro arquivo
rest_word -> resto da palavra/codigo que estiver na folha

"""
############################
class NodeTrie(object):
    def __init__(self,value,children_r= None, children_l = None , offsets =[] , rest_word = []):
        self.value = value
        self.children_r = children_r
        self.children_l = children_l
        self.offsets = offsets
        self.rest_word = rest_word
##############################
# search -> faz a busca do codigo binario na arvore
#
##############################     
    def search(self, code_bin):

        if code_bin[0] == '0':
            if self.children_l != None:
                if len(code_bin[1:]) > 0:
                    return self.children_l.search(code_bin[1:])
                else:
                    return [True , self.children_l]
            else:
                return [False, None]
        elif code_bin[0] == '1':
            if self.children_r != None:
                if len(code_bin[1:]) > 0:
                    return self.children_r.search(code_bin[1:])
                else:
                    return [True, self.children_r]
            else:
                return [False, None]
        return [None, "code invalid"] # se nao for 0 ou 1, ta errado
################################
# AddCodeBin => adiciona codigo caso ele nao exista
#
###############################

    def AddCodeBin(self, code, word, offset):
        if code[0] == '0':
            if self.children_l != None:
                if len(code[1:]) > 0:
                    return self.children_l.AddCodeBin(code[1:], word, offset)
            elif len(code[1:]) > 0:
                self.children_l = NodeTrie(code[0], offsets=[])
                self.children_l.AddCodeBin(code[1:] , word, offset)
            else:
                self.children_l = NodeTrie(code[0], offsets=[])
                self.children_l.offsets.append(offset)
                self.children_l.rest_word = word
        elif code[0] == '1':
            if self.children_r != None:
                if len(code[1:]) > 0:
                    return self.children_r.AddCodeBin(code[1:],word,offset)
            elif len(code[1:]) > 0:
                self.children_r = NodeTrie(code[0], offsets=[])
                self.children_r.AddCodeBin(code[1:],word,offset)
            else:
                self.children_r = NodeTrie(code[0], offsets=[])
                self.children_r.offsets.append(offset)
                self.children_r.rest_word                 
##################################
# AddNodeWord => Pega palavra coloca em hash e depois em binario
# Mais detalhes no comentarios a seguir
####################################

    def AddNodeWord(self,word,offset):
        
        hash_w = hashlib.md5(word.encode()) # UTF-8 necessita de encode antes
        hash_w_bin = bin(int(hash_w.hexdigest(),16)) # Deixa codigo em hexa
        # Para isso ele transforma em inteiro e depois em bits (str)
        hash_w_bin = hash_w_bin[2:]
        # Faz a procura se ja existe e offset nao ta na lista de offsets
        # Se ja tem e offset ta,coloca novo offset na lista de offsets 
        node = self.search(hash_w_bin)
        if node[0]:
            if offset not in node[1].offsets:
                node[1].offsets.append(offset)
        else:
            self.AddCodeBin(hash_w_bin, word, offset)

#########################################
"""
Classe com registro do arquivo, link, video e offset
"""
#########################################
class Register(object):
    def __init__(self,offset=0,info=[]):
        self.offset = offset 
        self.link = info[0]
        self.namevideo = info[1]
################################
# Register.link => link do video dos registros
# Register.namevideo => nome do videos dos registros
################################
    def __repr__(self):
        return "%s\t%s\t" % (str(self.namevideo)) , (str(self.link))
################################
# Funcoes auxiliares
################################
# normalize(titulo)=>texto em minusculo
#   pega o titulo do video e coloca em minusculo
################################

def normalize(title):
    aux_title = title.lower()

    word_list = re.sub("[\W]"," ",aux_title).split()

    return word_list
###############################
#
#
###############################

def intercession(listas):
    result = []
    a = listas[0]
    if len(listas[1:]) > 0:
        b = listas[1]
        for obj in a:
            if obj in b:
                result.append(obj)
        if len(listas[2:]) > 0:
            c = listas[2:]
            c.append(result)
            return intercession(c)
        else:
            return result
    else:
        return result

#############################################
# make_index_files => monta os arquivos indexados, que armazenam indices em TRIE
#
#############################################
def make_index_files(lista_de_registros, handler):
    trie_words = NodeTrie(None,offsets=[])
    trie_links = NodeTrie(None,offsets=[])
    trie_namevideos = NodeTrie(None,offsets=[])

    f_words = open(handler + "data_word_index.bin", 'wb')
    f_links = open(handler + "data_links_index.bin",'wb')
    f_namevideos = open(handler + "data_name_videos_index.bin",'wb')

    for registro in lista_registros:

        video_name = registro.namevideo # pega titulo do video
        video_n = normalize(video_name)
        for word in video_n:# para cada palavra, insere na trie e da um novo offset
            trie_words.AddNodeWord(word, registro.offset)

        trie_namevideos.AddNodeWord(registro.namevideo.lower(),registro.offset)
        trie_links.AddNodeWord(str(registro.link),registro.offset)

    pickle.dump(trie_words,f_words,pickle.HIGHEST_PROTOCOL)
    pickle.dump(trie_namevideos,f_namevideos,pickle.HIGHEST_PROTOCOL)
    pickle.dump(trie_links,f_links,pickle.HIGHEST_PROTOCOL)

    f_words.close()
    f_links.close()
    f_namevideos.close()

###########################################################################

def search_video(offset, name_file):

    handler = open(name_file + 'Data.bin','rb')

    for i in range(offset):
        pickle.load(handler)

    r = pickle.load(handler)

    handler.close()

    return r


##########################################################################

def list_video(word, tree, name_file):
    n = []
    videos = []


    hash_w = hashlib.md5(word.encode())
    hash_w_bin = bin(int(hash_w.hexdigest(),16))
    hash_w_bin = hash_w_bin[2:]

    n = tree.search(hash_w_bin)

    if n[0]:
        for i in n[1].offsets:
            videos.append(search_video(i,name_file))
        return videos
    else:
        return None
##########################################################################
# quick_sort => pega uma lista de registros e faz o ordenamento via quick
# separa a lista em 3 => menores, iguais e maiores
# Retorna a concatenacao das 3
##########################################################################
def quick_sort(lista_registro):
    less = []
    equal = []
    greater = []

    if len(lista_registro) > 1:
        pivot = lista_registro[0]
        for x in lista_registro:
            if x < pivot:
                less.append(x)
            if x == pivot:
                equal.append(x)
            if x > pivot:
                greater.append(x)

        return quick_sort(less)+equal+sort(greater)

    else:
        return lista_registro

###############################################################
def print_list(lista_registros):
    if(lista_registros == None):
        print ("\nRegistro nao encontrado.\n")
    else:
        if(len(lista_registros)> 15 ):
            sorted(lista_registros, key = lambda Register: Register.namevideo.lower())
        else:
            lista_registros = quick_sort(lista_registros)

    for registro in lista_registros:
        print ("%s\n") %(registro.namevideo)
