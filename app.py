#Importar classe restaurante


from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato



restaurante_praca = Restaurante('praca', 'Gourmet')
restaurante_praca.receber_avaliacoes('Gui', 5)
restaurante_praca.receber_avaliacoes('Lais', 4)
restaurante_praca.receber_avaliacoes('Emy', 2)

bebida_suco = Bebida('Suco de morango', 5.00, '300 ML')
prato_paozinho = Prato('Paozinho', 2.00, 'O melhor pão da cidade')

#Polimorfismo
bebida_suco.aplicar_desconto()
prato_paozinho.aplicar_desconto()


restaurante_praca.adicionar_item_no_cardapio(bebida_suco)
restaurante_praca.adicionar_item_no_cardapio(prato_paozinho)

#Pycache interpreta arquivos compilados em bytecode


def main():
    print(bebida_suco)
    print(prato_paozinho)
    Restaurante.listar_restaurantes()
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()