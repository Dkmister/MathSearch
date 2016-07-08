#   create_bin(c,n) = > c é a coluna, ou seja, conteudo que sera escrito, n é o nome do arquivo
#   abre arquivo, concatena com o nome sugerido
#   escreve conteudo e o fecha
def create_bin(conteudo,name):
    file = open(name+"csv_b.bin","wb")
    
    for element in conteudo:
        conte = str.encode(element+"\n")
        file.write(conte)
    file.close


