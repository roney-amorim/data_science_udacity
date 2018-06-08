# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import random
import pandas as pd
import numpy as np

# Lendo os dados como uma lista
print("Lendo o documento...")
data_list = pd.read_csv("titanic-data-6.csv")
total_passageiros = len(data_list)
print(total_passageiros)

#########################################################################################################

def count_people_by_class(data_list):
    '''
      Função que retorno a quantidade de pessoas de gêneros masculino e feminino identificada no data_list.
      Argumentos:
          data_list: Arquivo no formato de dictionary.
      Retorna:
          Quantidade de pessoas de gêneros masculino e feminino.
    '''
    first = 0
    second = 0
    third = 0

    for item in data_list:
        if item['Pclass'].title() == '1':
            first += 1
        elif item['Pclass'].title() == '2':
            second += 1
        elif item['Pclass'].title() == '3':
            third += 1
    return [first, second,third]

peoples = count_people_by_class(data_list)
print(peoples)

def count_people_by_class2(data_list):
    '''
      Função que retorno a quantidade de pessoas de gêneros masculino e feminino identificada no data_list.
      Argumentos:
          data_list: Arquivo no formato de dictionary.
      Retorna:
          Quantidade de pessoas de gêneros masculino e feminino.
    '''
    first = 0 
    second = 0
    third = 0

    for item in data_list:
        if item['Pclass'].title() == '1' and item['Survived'].title() == '1':
            first += 1
        elif item['Pclass'].title() == '2' and item['Survived'].title() == '1':
            second += 1
        elif item['Pclass'].title() == '3' and item['Survived'].title() == '1':
            third += 1
    return [first, second,third]

peoples2 = count_people_by_class2(data_list)
print(peoples2)

#########################################################################################################

def count_people_survived(data_list):
    '''
      Função que retorno a quantidade de pessoas de gêneros masculino e feminino identificada no data_list.
      Argumentos:
          data_list: Arquivo no formato de dictionary.
      Retorna:
          Quantidade de pessoas de gêneros masculino e feminino.
    '''
    survived = 0
    dead = 0
    for item in data_list:
        if item['Survived'].title() == '1':
            survived += 1
        if item['Survived'].title() == '0':
            dead += 1
        
    return [survived,dead]

print(count_people_survived(data_list))

'''
def count_people_by_class(classe):
    Função que retorno a quantidade de pessoas de gêneros masculino e feminino identificada no data_list.
    Argumentos:
        data_list: Arquivo no formato de dictionary.
    Retorna:
        Quantidade de pessoas de gêneros masculino e feminino.
    count_peoples = 0
    for item in data_list:
        if item['Pclass'].title() == classe:
            count_peoples += 1

    return count_peoples

first = count_people_by_class('1')
second = count_people_by_class('2')
third = count_people_by_class('3')
'''
#Quantas pessoas pertenciam a 1º classe
#Quantas pessoas pertenciam a 2º classe
#Quantas pessoas pertenciam a 3º classe  

#Quantas pessoas sobreviveram
#Quantas pessoas sobreviveram que pertenciam a 1º classe  
#Quantas pessoas sobreviveram que pertenciam a 2º classe  
#Quantas pessoas sobreviveram que pertenciam a 3º classe  

#Passos da análise de dados
#Pergunta
#Prepara
#Explorar
#Concluir
#Comunicar