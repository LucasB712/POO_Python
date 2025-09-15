# Sistema de Restaurante 🍽️

Este projeto simula um sistema básico de **restaurante** utilizando conceitos de **Programação Orientada a Objetos (POO)**, como **Polimorfismo**, **Herança** e **Encapsulamento**. O sistema permite:

- Criar restaurantes com avaliações de clientes.
- Adicionar itens (bebidas e pratos) ao cardápio.
- Aplicar descontos em itens do cardápio.
- Exibir o cardápio e listar os restaurantes cadastrados.

## Funcionalidades ✨

- **Adicionar Itens ao Cardápio**: Adiciona **bebidas** e **pratos** ao cardápio de um restaurante.
- **Receber Avaliações**: Os clientes podem avaliar o restaurante com notas de **1 a 5 estrelas**.
- **Aplicar Descontos**: O sistema aplica descontos automaticamente aos itens do cardápio.
- **Listar Restaurantes**: Exibe todos os restaurantes cadastrados no sistema.
- **Exibir Cardápio**: Exibe os itens no cardápio de um restaurante específico.

## Como Usar 🚀

### Passo 1: Instalar Dependências

Primeiro, instale as dependências do projeto. Caso haja um arquivo `requirements.txt`, você pode instalá-las com o comando:

```bash
pip install -r requirements.txt
```
Passo 2: Executar o Sistema
O script principal pode ser executado diretamente. Ao rodá-lo, o sistema exibirá as informações sobre o restaurante e os itens do cardápio.

```bash
python main.py
```
Exemplo de Saída
```bash
Bebida: Suco de Morango
Preço: R$ 5.00
Volume: 300 ML
Preço com desconto: R$ 4.50

Prato: Pãozinho
Preço: R$ 2.00
Descrição: O melhor pão da cidade
Preço com desconto: R$ 1.80

Restaurantes cadastrados:
- Praça Gourmet

Cardápio do Restaurante Praça Gourmet:
- Suco de Morango
- Pãozinho
```
## Arquitetura 📂
O projeto está estruturado da seguinte maneira:
```bash
├── modelos/
│   ├── __init__.py
│   ├── restaurante.py
│   └── cardapio/
│       ├── __init__.py
│       ├── bebida.py
│       └── prato.py
├── main.py
└── requirements.txt
```
restaurante.py: Contém a classe Restaurante, que gerencia as avaliações e o cardápio.

bebida.py: Contém a classe Bebida, representando uma bebida no cardápio.

prato.py: Contém a classe Prato, representando um prato no cardápio.

## Conceitos Utilizados 🧠

Polimorfismo
O polimorfismo é utilizado na aplicação de descontos. O método aplicar_desconto é comum tanto para bebidas quanto para pratos, mas a implementação é diferente para cada tipo de item, permitindo que o sistema trate ambos de forma uniforme.

Herança
As classes Bebida e Prato herdam de uma classe base, o que permite que compartilhem métodos comuns e adicionem funcionalidades específicas.

Encapsulamento
O encapsulamento é utilizado para ocultar detalhes internos da implementação, facilitando a interação com o sistema sem a necessidade de acessar diretamente os dados internos.

