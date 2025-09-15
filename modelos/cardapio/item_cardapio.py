from abc import ABC, abstractmethod

class ItemCardapio(ABC):
    def __init__(self, nome, preco):
        self._nome = nome
        self._preco = preco

    #Só para as derivadas/ Método abstrato
    @abstractmethod
    def aplicar_desconto():
        pass