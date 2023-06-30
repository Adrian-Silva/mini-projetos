import json
import requests

# Faz a requisição para a API
url = 'https://raw.githubusercontent.com/codeforamerica/click_that_hood/master/public/data/brazil-states.geojson'
response = requests.get(url)

# Verifica se a requisição foi bem-sucedida
if response.status_code == 200:
    # Lê os dados JSON da resposta
    data = response.json()

    # Grava os dados em um arquivo local
    with open('dados_estados_brasil.json', 'w') as file:
        json.dump(data, file, indent=4)
        print("Arquivo JSON gravado com sucesso!")
else:
    print("Não foi possível obter os dados da API.")
