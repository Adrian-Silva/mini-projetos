from flask import Flask

app = Flask(__name__)

# Configurações
app.config['SECRET_KEY'] = 'chave_secreta'

# Importar as rotas e modelos
from app import views
