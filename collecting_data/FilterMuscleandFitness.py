import pandas as pd

df = pd.read_csv('MuscleandFitness.csv')

word = input("Escreva a palavra desejada: ")

count = 0
count_columns = 0

# tf = True or False

# Crio um laço de repetição para calcular a quantidade de vezes que a palavra desejada aparece e em quantos artigos

for column in df['Texto']:
    #tf = word in column
    if word in column:
        count_columns += 1
        count += 1

    #print(tf)
    print(count)
    
print('Quantidade de artigos que localizaram a palavra',word,'foram:',count_columns)
