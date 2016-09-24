Este diretório diz a respeito da criação de um programa que classifica dados e organiza a partir de um arquivo csv que será transformado em binário para leitura 
e depois indexação através de arquivos sequenciais com arvores B/B++ e Patricia.

Bem-vindo ao CPD_MATH_S wiki! / Welcome to CPD_MATH_S wiki!
# Motivação:
Este trabalho foi motivado a partir da falta de recursos para conseguir acesso a um banco de dados de objetos matemáticos, no caso links de YouTube dos canais MeSalva e TodaAMatematica
# Antes de começar:
É necessário que tenha instalado Python 3-5 em seu computador e a biblioteca pandas.<br>
Python 3-5 : https://www.python.org/downloads/<br>
pandas(Linux/Windows/MAC): http://pandas.pydata.org/pandas-docs/stable/install.html<br>

# Como usar:
Para usar o MathSearch , é necessário clonar o diretório contido em seu local preferido no seu computador.

No terminal/cmd selecione o diretório e execute o seguinte comando:

```bash
$ python3 main.py
```

Logo em seguida, será perguntando qual o nome desejado do arquivo de saída para visualização dos dados.<br>
Selecione o nome de sua preferência.
Aparecerá o menu com escolha:


    1. Listagem de todos vídeos
    2. Busca por substring nos vídeos
    99. Sair do programar


Ao buscar pela substring de vídeos com conteúdo similiar, irá aparecer na tela para que o usuário insira a palavra que quer buscar.


Ao fim aparecerá o nome dos vídeos que contem a substring. No arquivo estará o link ao lado do nome deles.<br>

Os resultados estarão dentro do arquivo .txt selecionado
