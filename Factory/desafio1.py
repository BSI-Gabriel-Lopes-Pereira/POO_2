from abc import ABC, abstractmethod

class MetodoPagamento(ABC):
    @abstractmethod
    def pagar(self, valor):
        pass

class CartaoCredito(MetodoPagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado com Cartão de Crédito.")

class PayPal(MetodoPagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado com PayPal.")

class Boleto(MetodoPagamento):
    def pagar(self, valor):
        print(f"Pagamento de R${valor} realizado com Boleto.")

class FabricaPagamento(ABC):
    @abstractmethod
    def criar_pagamento(self):
        pass

class FabricaCartaoCredito(FabricaPagamento):
    def criar_pagamento(self):
        return CartaoCredito()

class FabricaPayPal(FabricaPagamento):
    def criar_pagamento(self):
        return PayPal()

class FabricaBoleto(FabricaPagamento):
    def criar_pagamento(self):
        return Boleto()

if __name__ == "__main__":
    valor = 100

    fabrica_pagamento = FabricaCartaoCredito()
    pagamento = fabrica_pagamento.criar_pagamento()
    pagamento.pagar(valor)

    fabrica_pagamento = FabricaPayPal()
    pagamento = fabrica_pagamento.criar_pagamento()
    pagamento.pagar(valor)

    fabrica_pagamento = FabricaBoleto()
    pagamento = fabrica_pagamento.criar_pagamento()
    pagamento.pagar(valor)
