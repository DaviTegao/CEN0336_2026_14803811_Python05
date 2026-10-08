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

#coisa_fav = input('Qual seu tipo de coisa favorita?: ') # Cria um imput que pergunta ao usuario na linha de comando qual seu tipo de coisa favorita, podendo ser qualquer uma das chaves presentes no dicionarios, que foram listadas anteriormente
#print('Sua coisa favorita é: ',Favoritos[coisa_fav]) # Responde com o valor correspondente a chave digitada pelo usuario na linha de comando

## 7

Favoritos['Organismo'] = 'Deinonychus' # Muda o valor da chave 'Organismo' de 'Archaeopteryx' para 'Deinonychus'
print(Favoritos['Organismo']) #Imprime o novo valor para a chave 'Organismo' do dicionario

## 8

print('Lista de tipos de coisas favoritas:')
for coisa in Favoritos: # Cria um loop que imprime todas as possiveis coisas favoritas (chaves)
   print (coisa)

#coisa_fav = input('Qual seu tipo de coisa favorita?: ') # Cria um imput que pergunta ao usuario na linha de comando qual seu tipo de coisa favorita, podendo ser qualquer uma das chaves presentes no dicionarios, que foram listadas anteriormente
#Favoritos[coisa_fav] = input(f'Qual seu(a) {coisa_fav} Favorito(a): ') # Atribui ao dicionario, na chave escolhina na linha anterior, na variavel 'coisa_fav' um novo valor, a partir de um input do usuario na linha de comando 
#print('Seu(a)', coisa_fav, 'favorito(a) é:', Favoritos[coisa_fav])  # Responde a coisa favorita do usuario, para a chave escolhida por ele

## 9

for coisa in Favoritos:  # Cria um loop que mostra todas a chaves e valores do dicionario 'Favoritos'
   seq = Favoritos[coisa]
   print(coisa, seq[0:10])

## 10

mySet = set('ATGTGGG')
mySet2 = {'ATGCCT'}

print(mySet)
print(mySet2)

# A diferença entre as duas sintaxes está na forma em que os elementos são salvos no conjunto, enquanto a mySet2(= {sequencia}) cataloga toda a sequencia de nucleotidios como um unico elemento de dado, a mySet(= set(sequencia)) separa as letras da sequencia individualmente, e adiciona ao conjunto apenas as letras diferentes umas da outras.

## 11

SetA = {3, 14, 15, 9, 26, 5, 35, 9} # Gera o conjunto SetA
SetB = {60, 22, 14, 0, 9} # Gera o conjunto SetB

difAB = SetA - SetB # Calcula a deferença entre SetA e SetB
difBA = SetB - SetA # Calcula a diferença entre SetB e SetA
uni = SetA | SetB # Calcula a diferença entre os conjuntos
int = SetA & SetB # Calcula a união entre os conjuntos
difsim = SetA ^ SetB # Calcula a diferença simétrica entre os conjuntos

print('A diferença entre SetA e SetB é:', difAB) # Imprime os valores obtidos
print('A diferença entre SetB e SetA é:', difBA)
print('A união entre SetA e SetB é:', uni)
print('A intersesão entre SetA e SetB é:', int)
print('A diferença simétrica entre SetA e SetB é:', difsim)

## 12

SeqA = {'GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC'}
SeqB = set('GATGGGATTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGACAGAAACACTTTTCGTGGGGTTTTCCCCTCCCATGTGCTCAAGACTGGCGCTAAAAGTTTTGAGCTTCTCAAAAGTCTAGAGCCACCGTCCAGGGAGCAGGTAGCTGCTGGGCTCCGGGGACACTTTGCGTTCGGGCTGGGAGCGTGCTTTCCACGACGGTGACACGCTTCCCTGGATTGGCAGCCAGACTGCCTTCCGGGTCACTGCCATGGAGGAGCCGCAGTCAGATCCTAGCGTCGAGCCCCCTCTGAGTCAGGAAACATTTTCAGACCTATGGAAACTACTTCCTGAAAACAACGTTCTGTCCCCCTTGCCGTCCCAAGCAATGGATGATTTGATGCTGTCCCCGGACGATATTGAACAATGGTTCACTGAAGACCCAGGTCCAGATGAAGCTCCCAGAATTCGCCAGAGGCTGCTCCCCCCGTGGCCCCTGCACCAGCAGCTCCTACACCGGCGGCCCCTGCACCAGCCCCCTCCTGGCCCCTGTCATCTTCTGTCCCTTCCCAGAAAACCTACCAGGGCAGCTACGGTTTCCGTCTGGGCTTCTTGCATTCTGGGACAGCCAAGTCTGTGACTTGCACGTACTCCCCTGCCCTCAACAAGATGTTTTGCCAACTGGCCAAGACCTGCCCTGTGCAGCTGTGGGTTGATTCCACACCCCCGCCCGGCACCCGCGTCCGCGCCATGGCCATCTACAAGCAGTCACAGCACATGACGGAGGTTGTGAGGCGCTGCCCCCACCATGAGCGCTGCTCAGATAGCGATGGTCTGGCCCCTCCTCAGCATCTTATCCGAGTGGAAGGAAATTTGCGTGTGGAGTATTTGGATGAC')

print(SeqA)
print(SeqB)

# Como visto anteriormente, na pergunta 10, os conjuntos podem ser gerados de duas maneiras diferentes, quando fazemos por (={sequencia}), obtemos um conjunto com apenas um unico elemento, sendo este a sequencia completa, Ja no modelo (=set(sequencia)), obtemos apenas os diferentes elementos presentes na sequencia, sendo {A, C, G, T}. 

## 13

seq = ('GAACTCCAAAAATGAAAACATAGTAGCAATCAAAGCATCCCACTATTTTTTGTCTCTCGTTTCATTAGCGTTGTAAATTACTGATACCCTACTATACCTCTACAAGGCCTTTGTCATCTTTTTACTCAAGTGTGAAATCATCACTTATTGTATGAAGGATGAGCTTTCCGTTCGCTAGTTTGCTGAAAAGGCCTTCTGCAATAAGCTCTCTATTATCTTTAAAAAAACCTGGTTCCTGGTCTTCCATTCTGCTAAAAGCTGTAGGGGTTTTATCACGAGATTCCCGTTGGCATTCTGACTTATTAAAAATGCTTACAGAAGAAATGGATTCTTTAAATGGTCAAATTAATACGTGGACAGATAATAATCCTTTATTAGATGAAATTACGAAGCCATACAGAAAATCTTCAACTCGTTTTTTTCATCCGCTTCTTGTACTTCTAATGTCTAGAGCATCAGTAAATGGGGATCCACCGAGTCAGCAACTATTTCAAAGGTACAAACAACTTGCCCGTGTAACAGAATTGATTCATGCTGCCAATATAATTCATATTAATATTGGAGAAGAACAAAGCAACGAACAGATTAAACTTGCAACGTTGGTTGGAGATTATTTACTCGGAAAGGCGTCTGTTGATTTAGCACATTTAGAAAACAACGCTATTACAGAAATTATGGCTTCTGTTATTGCAAACTTAGTTGAAGGGCACTTCGGAAGCCGACAAAATGGCTCTGTTGGTTTGTCAAACGAACGAACCATCCTTCTGCAATCAGCCTTTATGCCAGCAAAGGCATGTTTATGCGCAAGCATATTGAATAACTCATCACAATACATTAATGATGCGTGTTTCAATTATGGAAAATTTCTAGGCTTATCGCTGCAACTGGCCCATAAGCCTGTATCTCCTGACGCCCAAGTTTTGCAAAAGAATAATGACATTTTGAAAACATATGTTGAGAATGCCAAGAGCTCATTGTCTGTTTTCCCCGATATAGAGGCTAAGCAAGCTCTCATGGAAATCGCTAATAGTGTTTCGAAGTAATCGACAGGTATTGTATCCTGGATTAATATTAGGGTGGCTCATGCATGCTCGTGCAATCGTAACAAATATGTCTTTCTTTTACGAATTTTAACGCTTCAATATAAATCATATTTTTCCTCA')
seqcon = set(seq)
print(seqcon) # Imprime o conjunto gerado na linha acima, de moda a apresentar apenas os caracteres unicos da sequencia

count = {} # Gera um dicionario vazio para fazer a contagem

for nt in seq: # Gera um loop de contagem de nucleotidios na sequencia
   if nt in count: # Caso aquela letra (nucleotidio) ja esta no dicionario)
      anterior = count[nt] # Verifica o numero atula da contagem para aquele nucleotido no dicionario
      novo = anterior+1 # Estabelece o novo valor de contagem como o anterior +1
      count[nt] = novo # Adiciona o novo valor ao dicionario
   else: # Caso aquele nucleotidio ainda não esteja presente no dicionario
      count[nt] = 1; # Atribui o valor 1 a contagem deste novo nucleotidio ao dicionario

print(count) # Imprime o dicionario, agora com as contagens
print('A sequencia de DNA é composta por:', count['A'], 'Adeninas,', count['T'], 'Timinas,', count['C'], 'Citosinas e', count['G'], 'Guaninas')
gc = count['C'] + count['G']
total = count['A'] + count['T'] + count['C'] + count['G']
prop = gc/total*100

print('Na sequencia temos uma quantidade de GC de', gc, ', em um total de', total, 'nucleotídios, com um proporção de', prop, '%')
