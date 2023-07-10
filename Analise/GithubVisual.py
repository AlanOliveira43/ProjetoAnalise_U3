from pyvis.network import Network
import requests
import json

# URL do repositório no GitHub
repo_url = 'https://github.com/tensorflow/tensorflow'

# Fazendo uma solicitação GET para obter os dados do repositório
response = requests.get(repo_url)

# Verificando se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Convertendo a resposta em formato JSON
    repo_data = json.loads(response.text)
    
    # Criando uma instância do grafo
    graph = Network(height='800px', width='100%')

    # Adicionando o nó do repositório
    graph.add_node(repo_data['name'], shape='box', title=repo_data['description'])
    
    # Obtendo as informações dos contribuidores do repositório
    contributors_url = repo_data['contributors_url']
    contributors_response = requests.get(contributors_url)
    
    if contributors_response.status_code == 200:
        contributors_data = json.loads(contributors_response.text)
        
        # Adicionando os nós dos contribuidores
        for contributor in contributors_data:
            graph.add_node(contributor['login'], shape='circle', title=contributor['html_url'])
            graph.add_edge(contributor['login'], repo_data['name'])
    
    # Exibindo o grafo
    graph.show('graph.html')
else:
    print('Erro ao obter dados do repositório')
