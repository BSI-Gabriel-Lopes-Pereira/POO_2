# Implemente uma calculadora de impostos que use o padrão Strategy para aplicar diferentes tipos de
# impostos (por exemplo, imposto sobre renda, imposto sobre vendas, imposto sobre produtos).

from abc import ABC, abstractmethod

class ImpostoStrategy(ABC):
    @abstractmethod
    def calcular(self, valor: float) -> float:
        pass

class ImpostoRenda(ImpostoStrategy):
    def calcular(self, valor: float) -> float:
        return valor * 0.20

class ImpostoVendas(ImpostoStrategy):
    def calcular(self, valor: float) -> float:
        return valor * 0.10

class ImpostoProduto(ImpostoStrategy):
    def calcular(self, valor: float) -> float:
        return valor * 0.15

class CalculadoraDeImposto:
    def __init__(self, strategy: ImpostoStrategy = None):
        self._strategy = strategy

    def set_imposto_strategy(self, strategy: ImpostoStrategy):
        self._strategy = strategy

    def calcular_imposto(self, valor: float) -> float:
        if not self._strategy:
            raise ValueError("A estratégia de imposto não foi definida.")
        return self._strategy.calcular(valor)

def main():
    print("Escolha o tipo de imposto:")
    print("1 - Imposto de Renda (20%)")
    print("2 - Imposto sobre Vendas (10%)")
    print("3 - Imposto sobre Produtos (15%)")

    choice = input("Digite o número correspondente ao tipo de imposto: ")
    valor = float(input("Digite o valor sobre o qual será calculado o imposto: "))

    calculadora = CalculadoraDeImposto()

    if choice == '1':
        calculadora.set_imposto_strategy(ImpostoRenda())
    elif choice == '2':
        calculadora.set_imposto_strategy(ImpostoVendas())
    elif choice == '3':
        calculadora.set_imposto_strategy(ImpostoProduto())
    else:
        print("Escolha inválida.")
        return

    imposto = calculadora.calcular_imposto(valor)
    print(f"O valor do imposto é: R$ {imposto:.2f}")

if __name__ == "__main__":
    main()
