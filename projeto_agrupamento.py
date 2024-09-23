# -*- coding: utf-8 -*-
"""Projeto Agrupamento

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1AUgQlFNCv32VYxjqkhf7rDnDfSRedIou
"""

# Importando

# Numpy
import numpy as np

#KMeans
from sklearn.cluster import KMeans
filmes_assistidos = np.array([
    [1, 0, 0, 1, 0, 1], #Usuário 1: Assistiu aos filmes 1 e 4
    [1, 1, 0, 0, 1, 1], #Usuário 2: Assistiu aos filmes 1 e 2
    [0, 1, 1, 0, 0, 0], #Usuário 3: Assistiu aos filmes 2 e 3
    [0, 0, 1, 1, 1, 0], #Usuário 4: Assistiu aos filmes 3 e 4
    [1, 0, 1, 0, 0, 0], #Usuário 5: Assistiu aos filmes 1 e 3
    [0, 1, 0, 1, 1, 0] #Usuário 6: Assistiu aos filmes 2 e 4
])

# Treinar o modelo
num_clusters = 2

#iniciando o modelo
kmeans = KMeans(n_clusters=num_clusters,
                random_state=0,n_init=10)

# treinando o modelo
kmeans.fit(filmes_assistidos)

#classificando os usuários
grupos_indice = kmeans.predict(filmes_assistidos)

#Exibir os dados
print("Usuário pertencente ao seguinte grupo")
for i, cluster in enumerate(grupos_indice):
    print(f"Usuário {i+1}: Grupo {cluster+1}")

print("\nFilmes assistidos:")
for i in range(len(filmes_assistidos)):
    assistidos = np.where(filmes_assistidos[i] == 1)[0] + 1
    print(f"Usuário {i+1}n assistiu aos filmes: {assistidos}")

# Função que recomenda filmes
def recomendar_filmes(filmes, filmes_assistidos, grupos_indice):
   filmes = np.array(filmes)

   #Encontrar o grupo do usuário com base em seu vetor de filmes
   usuario_id = len(filmes_assistidos)
   grupo_usuarios = kmeans.preditc([filmes])[0]

   #Encontrar todos osn usuarios no mesmo grupo
   usuarios_no_mesmo_grupo = [i for i in range(len(grupos_indice))
   if grupos_indice[i] == grupo_usuarios]

   #Filmes assistidos pelos usuarios no mesmo grupo
   filmes_recomendados = set()
   for usuario in usuarios_no_mesmo_grupo:
    filmes_assistidos_usuario = np.where(filmes_assistidos[usuario] == 1)[0]
    filmes_recomendados.update(filmes_assistidos_usuario)

    #Remover filmes que o usuaro ja assistiu
    filmes_recomendados = filmes_recomendados - set(np.where(filmes_assistidos == 1)[0])

    #ajustar os indices dos filmes recomendados (de volta para a 1-based)
    filmes_recomendados = [filme + 1 for filme in filmes_recomendados]

    return sorted(filmes_recomendados)

#exemplo de uso da fução recomendar_fillmes
filmes_assistidos_usuarios = [1, 0, 1, 0] # Vetor de filmes
#assistidos (por exemplo, assistiu aos filmes 1 e 3)
filmes_recomendados = recomendar_filmes(filmes_assistidos_usuarios, filmes_assistidos, grupos_indice)

print(f"\nfilmes recomendados: {filmes_recomendados}")