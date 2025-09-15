import requests
import json

#Alt z quebra a linha para uma melhor visualização

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)
print(response)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurante = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurante:
            dados_restaurante[nome_restaurante] = []
        
        dados_restaurante[nome_restaurante].append({
            "item": item['Item'],
            "preco": item['price'],
            "descricao": item['description']
        })
else:
    print(f'O Erro foi {response.status_code}')

#print(dados_restaurante['Pizza Hut'])

for nome_restaurante, dados in dados_restaurante.items():
    nome_arquivo = f'{nome_restaurante}.json'
    #Manipular e criar arquivos. Queremos escrever, ler...
    with open(nome_arquivo, 'w') as arquivo_restaurante:
        #Dump gera esse dado
        json.dump(dados, arquivo_restaurante, indent = 4)
