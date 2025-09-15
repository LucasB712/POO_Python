from fastapi import FastAPI, Query
import requests, json

app = FastAPI()

@app.get('/api/hello')
def hello_world():
    '''Endpoint de Hello World'''
    return {'Hello':'World'} 

@app.get('/api/restaurantes/')
def get_restaurantes(restaurante: str = Query(None)):
#Alt z quebra a linha para uma melhor visualização
    url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

    '''Endpoint para ver os cardápios dos restaurantes'''
    
    response = requests.get(url)
    print(response)

    if response.status_code == 200:
        dados_json = response.json()
        
        if restaurante is None:
            #Passa o caradápio todo
            return {'Dados': dados_json}
         
        dados_restaurante = []
        for item in dados_json:
            if item['Company'] == restaurante:
                dados_restaurante.append({
                    "item": item['Item'],
                    "preco": item['price'],
                    "descricao": item['description']
                })
        return {'Restaurante' : restaurante, 'Cardápio' : dados_restaurante}
    else:
        return {'Erro' : f'{response.status_code} -- {response.text}'}