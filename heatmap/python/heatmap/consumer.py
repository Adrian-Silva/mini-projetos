import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import numpy as np
from PIL import Image

url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
response = requests.get(url)
data = response.json()

# Cria um objeto GeoDataFrame a partir do arquivo GeoJSON
gdf = gpd.GeoDataFrame.from_features(data['features'])

# Encontra o índice correspondente ao estado de São Paulo
#sp_index = gdf[gdf['name'] == 'São Paulo'].index[0]

# Cria uma lista de valores aleatórios para os estados (substitua com seus dados reais)
valores = np.random.rand(len(gdf))

# Define a cor do mapa com base nos valores dos estados
min_value = min(valores)
max_value = max(valores)

# Escolha um mapa de cores adequado
# O mapa de cores 'YlOrRd' é uma abreviação de "Yellow-Orange-Red" e é um mapa de cores sequencial que varia de amarelo a laranja e, finalmente, para vermelho.
cmap = plt.get_cmap('YlOrRd')

# A função plt.Normalize() é uma função do Matplotlib que realiza a normalização dos valores.
normalize = plt.Normalize(vmin=min_value, vmax=max_value)

# Cria uma lista de cores correspondentes aos valores dos estados, com base no mapa de cores (cmap) e na normalização (normalize) aplicados aos valores.
# O valor é passado para a função normalize, que mapeia esse valor normalizado em um valor proporcional na escala de cores definida pelo vmin e vmax.
# O valor normalizado é então passado para o mapa de cores (cmap) por meio da chamada de função cmap(normalize(value)). Isso retorna a cor correspondente para aquele valor na escala de cores definida.
colors = [cmap(normalize(value)) for value in valores]

# Plota o mapa de estados com cores personalizadas
fig, ax = plt.subplots(figsize=(10, 10))
gdf.plot(ax=ax, linewidth=0.8, edgecolor='0.8', facecolor=colors)

# Personaliza o gráfico
ax.axis('off')

# Salva a figura como um arquivo PNG
plt.savefig('mapa.png', bbox_inches='tight', pad_inches=0)

# Fecha a figura para liberar memória
plt.close(fig)

# Carrega a imagem salva como um objeto Image
image = Image.open('mapa.png')

# Exibe a imagem
image.show()
