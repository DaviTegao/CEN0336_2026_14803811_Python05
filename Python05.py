#!/usr/bin/env python3
import sys

## Relatorio Python 5 Davi Tegão - 14803811

## 1

Favoritos = { 
               'Livro':'Palavras de Radiancia',
               'Arvore':'Mangueira',
               'Musica':'Duality'}   # Cria um dicionario com minhas coisas favoritas, no formato {chave: valor}

print(Favoritos) # Imprime o dicionario criado

## 2

print(Favoritos['Livro']) # Imprime o valor para a chave 'Livro' do dicionario criado

## 3

coisa_fav = 'Livro' # atribui a chave 'Livro' a uma variavel
print(Favoritos[coisa_fav]) # Imprime o valor para a chave 'Livro' a partir da variavel criada

## 4 

print(Favoritos['Arvore']) #Imprime o valor para a chave 'Arvore' do dicionario

## 5

Favoritos['Organismo'] = 'Archaeopteryx'  # Adiciona uma nova chave e valor ao dicionario, sendo: {'Organismo': 'Archaeopteryx'}
print(Favoritos) # Imprime o dicionario completo com a nova chave e valor

coisa_fav = 'Organismo'
print(Favoritos[coisa_fav]) # Imprime o valor para a chave 'Organismo' a partir da variavel 'coisa_fav'

## 6


print('Lista de tipos de coisas favoritas:')
for coisa in Favoritos: # Cria um loop que imprime todas as possiveis coisas favoritas (chaves)
   print (coisa)

coisa_fav = input('Qual seu tipo de coisa favorita? ') # Cria um imput que pergunta ao usuario na linha de comando qual seu tipo de coisa favorita, podendo ser qualquer uma das chaves presentes no dicionarios, que foram listadas anteriormente
print('Sua coisa favorita é: ',Favoritos[coisa_fav]) # Responde com o valor correspondente a chave digitada pelo usuario na linha de comando
