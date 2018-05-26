# coding: utf-8

# Começando com os imports
import csv
import matplotlib.pyplot as plt
import random
import pandas as pandas
import numpy as np

# Vamos ler os dados como uma lista
print("Lendo o documento...")
with open("titanic-data-6.csv", "r") as file_read:
    data_list = [{k: v for k, v in row.items()} 
        for row in csv.DictReader(file_read, skipinitialspace=True)]
print(data_list)


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