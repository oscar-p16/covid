# -*- coding: utf-8 -*-
"""
Created on Mon Nov 29 19:46:25 2021

@author: oscar perez
"""

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

url = 'covid_22_noviembre.csv'

data = pd.read_csv(url)

url = 'covid_22_noviembre.csv'

data = pd.read_csv(url)

#-----------------------------------------------------------
#Número de casos de Contagiados en el País.
num_pais = len(data)

print(" 1")

print(num_pais)

print() 

num_pais = len(data)

print(" 1")

print(num_pais)

print()
 
#-----------------------------------------------------------
#Número de Municipios Afectados

num_muni = len(data.groupby('Nombre').size())

print("2")

print(num_muni)

print() 

