#!/usr/bin/env python
# -*- coding: utf-8 -*-


#Code by Arthur L.
#Comentariso by Vilmar
#funcao pra abrir e ler csv e transformar em bin
with open('Math_Application_CPD.csv', encoding='utf-8', mode='r') as file:
    with open('result.bin', 'wb') as final:
        for x in file:
            final.write(file.readline().encode('utf-8'))
    final.close()
file.close()
#decodificar bin com utf-8
with open('result.bin', 'rb') as f:
    for y in f:
        data = (f.readline().decode('utf-8'))
        print(data)
