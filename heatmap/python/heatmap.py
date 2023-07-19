import pandas as pd
import geopandas as gpd
import matplotlib.pyplot as plt
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import numpy as np
import io
import base64

# URL do arquivo GeoJSON contendo as fronteiras dos estados do Brasil
url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
response = requests.get(url)
data = response.json()

# Cria um GeoDataFrame a partir dos dados do GeoJSON
gdf = gpd.GeoDataFrame.from_features(data['features'])

# Cria um DataFrame com as informações que você deseja plotar
df_heatmap = pd.DataFrame({
    'region_iam': ['SP - RJ', 'ES', 'AM', 'SC', 'RS - MG'],
    'total_nav_moeda_fundo': [10.0, 20.0, 30.0, 40.0, 50.0]
})

df_heatmap['region_iam'] = df_heatmap['region_iam'].str.split(' - ')
df_heatmap['total_nav_moeda_fundo'] = df_heatmap.apply(lambda row: row['total_nav_moeda_fundo'] / len(row['region_iam']), axis=1)
df_heatmap = df_heatmap.explode('region_iam')


# Define os valores mínimo e máximo para a normalização das cores
min_value = df_heatmap['total_nav_moeda_fundo'].min()
max_value = df_heatmap['total_nav_moeda_fundo'].max()

# Define a escala de cores a ser utilizada
cmap = plt.get_cmap('YlOrRd')

# Cria uma função de normalização com base nos valores mínimo e máximo
normalize = plt.Normalize(vmin=min_value, vmax=max_value)

# Aplica a função de normalização aos valores e obtém as cores correspondentes
colors = [cmap(normalize(value)) for value in df_heatmap['total_nav_moeda_fundo']]

# Cria uma figura e um eixo para o gráfico
fig, ax = plt.subplots(figsize=(10, 10))

# Plota as geometrias dos estados com as cores correspondentes
gdf.plot(ax=ax, linewidth=0.8, edgecolor='0.8', facecolor='gray')
gdf[gdf['sigla'].isin(df_heatmap['region_iam'])].plot(ax=ax, linewidth=0.8, edgecolor='0.8', facecolor=colors)

# Remove os eixos da figura
ax.axis('off')

# Exibe o mapa
plt.show()