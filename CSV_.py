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

        

