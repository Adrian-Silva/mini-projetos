# Arquitetura (MVC)
```
projeto/
│
├── app/
│   ├── __init__.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── report.py
│   │   ├── ...
│   ├── views/
│   │   ├── __init__.py
│   │   ├── views.py
│   │   ├── ...
│   └── templates/
│       ├── index.html
│       └── ...
│
├── static/
│   ├── css/
│   │   ├── style.css
│   │   └── ...
│   ├── js/
│   │   ├── script.js
│   │   └── ...
│   ├── images/
│   └── ...
│
└── run.py
```

# Arquivos

### `projeto/app/__init__.py`:

No Python, quando um pacote é importado, o interpretador procura pelo arquivo `__init__.py` dentro desse pacote e executa qualquer código presente nele. Portanto, ao importar o pacote app, o arquivo `__init__.py` dentro desse pacote é automaticamente executado. 

Se o seu pacote models contém várias classes de modelos importantes como User, Post e Comment, importá-las no arquivo `__init__.py` permite que os usuários do pacote as importem diretamente do pacote models:

```python
# app/models/__init__.py

from .user import User
from .post import Post
from .comment import Comment
```
Com isso, os usuários podem importar essas classes diretamente do pacote models em outras partes do código sem ter que especificar o módulo de origem:
```python
from app.models import User, Post, Comment
```
Agora no contexto da arquitetura atual o `__init__.py`

- Inicializa o aplicativo Flask.
- Define configurações globais do aplicativo, como a chave secreta.
- Importa as rotas e modelos do aplicativo.

### models.py:

- Este arquivo contém a definição dos modelos de dados do aplicativo.
- Define a classe Report, que representa um relatório com atributos como id, título e descrição.
- Inicializa uma lista de objetos Report, simulando dados de relatórios.

### views.py:

- Este arquivo define as rotas do Flask e as funções de visualização (controllers).
- Importa o objeto app do Flask e os dados de relatório do arquivo models.py.
- Define uma rota principal / que renderiza o template HTML index.html e passa a lista de relatórios para ser exibida na página.

### templates/index.html:

- Este arquivo contém o código HTML para a página principal do aplicativo.
- Utiliza a sintaxe do Jinja2 para renderizar os dados dinâmicos (lista de relatórios) passados pela função de visualização em views.py.
- Inclui referências a arquivos estáticos (CSS e JavaScript).

### static/css/style.css:

- Este arquivo contém estilos CSS para a página HTML.
- Define estilos de formatação, layout e design para os elementos na página.

### static/js/script.js:

- Este arquivo contém scripts JavaScript para a página HTML (opcional).
- Pode conter interações do lado do cliente, manipulações DOM, chamadas de API, etc.

### run.py:

- Este arquivo é usado para iniciar o servidor Flask.
- Importa o objeto app do Flask do arquivo __init__.py.
- Verifica se o script está sendo executado diretamente e, em seguida, inicia o servidor Flask em modo de depuração.
