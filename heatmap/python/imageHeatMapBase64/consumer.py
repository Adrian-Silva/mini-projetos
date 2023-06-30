import requests

def load_map_image():
    # Faz uma requisição para o servidor desejado
    response = requests.get('http://localhost:5000/get_map_image')
    
    if response.ok:
        # Obtém o conteúdo da resposta como um objeto blob
        blob = response.content
        
        # Grava o conteúdo no arquivo de texto
        with open('map_image.txt', 'wb') as file:
            file.write(blob)
        
        print("Arquivo gravado com sucesso.")
        
    else:
        raise ValueError('Erro na resposta do servidor')
        
try:
    load_map_image()
except Exception as e:
    print(f"Ocorreu um erro: {e}")
