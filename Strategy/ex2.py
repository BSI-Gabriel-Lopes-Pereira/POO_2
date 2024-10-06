# Usar o padrão Strategy para aplicar diferentes estratégias de desconto em um sistema de compras.

from abc import ABC, abstractmethod

class DiscountStrategy(ABC):
    @abstractmethod
    def apply_discount(self, total: float) -> float:
        pass

class LoyaltyDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total * 0.95

class SeasonalDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total * 0.90

class BulkPurchaseDiscount(DiscountStrategy):
    def apply_discount(self, total: float) -> float:
        return total * 0.85

class ShoppingCart:
    def __init__(self, strategy: DiscountStrategy = None):
        self._strategy = strategy

    def set_discount_strategy(self, strategy: DiscountStrategy):
        self._strategy = strategy

    def get_final_price(self, total: float) -> float:
        if not self._strategy:
            raise ValueError("A estratégia de desconto não foi definida.")
        return self._strategy.apply_discount(total)

def main():
    print("Escolha o tipo de desconto:")
    print("1 - Desconto por fidelidade (5%)")
    print("2 - Desconto sazonal (10%)")
    print("3 - Desconto por grandes volumes (15%)")

    choice = input("Digite o número correspondente ao tipo de desconto: ")
    total = float(input("Digite o valor total da compra: "))

    cart = ShoppingCart()

    if choice == '1':
        cart.set_discount_strategy(LoyaltyDiscount())
    elif choice == '2':
        cart.set_discount_strategy(SeasonalDiscount())
    elif choice == '3':
        cart.set_discount_strategy(BulkPurchaseDiscount())
    else:
        print("Escolha inválida.")
        return

    final_price = cart.get_final_price(total)
    print(f"Valor final após desconto: R$ {final_price:.2f}")

if __name__ == "__main__":
    main()
