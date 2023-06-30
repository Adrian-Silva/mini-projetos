


import matplotlib
matplotlib.use('Agg')

from flask import Flask
import geopandas as gpd
import matplotlib.pyplot as plt
import requests
import numpy as np
import io
import base64

app = Flask(__name__)

@app.route('/get_map_image')
def get_map_image():
    # URL do arquivo GeoJSON contendo as fronteiras dos estados do Brasil
    url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
    response = requests.get(url)
    data = response.json()

    # Cria um GeoDataFrame a partir dos dados do GeoJSON
    gdf = gpd.GeoDataFrame.from_features(data['features'])

    # Gera valores aleatórios para cada estado
    valores = np.random.rand(len(gdf))

    # Define os valores mínimo e máximo para a normalização das cores
    min_value = min(valores)
    max_value = max(valores)

    # Define a escala de cores a ser utilizada
    cmap = plt.get_cmap('YlOrRd')

    # Cria uma função de normalização com base nos valores mínimo e máximo
    normalize = plt.Normalize(vmin=min_value, vmax=max_value)

    # Aplica a função de normalização aos valores e obtém as cores correspondentes
    colors = [cmap(normalize(value)) for value in valores]

    # Cria uma figura e um eixo para o gráfico
    fig, ax = plt.subplots(figsize=(10, 10))

    # Plota as geometrias dos estados com as cores correspondentes
    gdf.plot(ax=ax, linewidth=0.8, edgecolor='0.8', facecolor=colors)

    # Remove os eixos da figura
    ax.axis('off')

    # Cria um fluxo de bytes para armazenar a imagem
    image_stream = io.BytesIO()

    # Salva a figura no fluxo de bytes no formato PNG
    plt.savefig(image_stream, format='png')

    # Fecha a figura
    plt.close(fig)

    # Move o ponteiro do fluxo de bytes para o início
    image_stream.seek(0)

    # Converte a imagem para uma string codificada em base64
    image_base64 = base64.b64encode(image_stream.getvalue()).decode('utf-8')

    # Cria a URL da imagem codificada em base64
    image_url = f"data:image/png;base64,{image_base64}"

    # Retorna a URL da imagem como resposta
    return image_url

if __name__ == '__main__':
    app.run()
