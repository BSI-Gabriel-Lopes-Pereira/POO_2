# Criar um sistema que utilize o padrão Strategy para simular diferentes estratégias de deslocamento
# usando meios de transporte variados.

from abc import ABC, abstractmethod

class TravelStrategy(ABC):
    @abstractmethod
    def travel_time(self, distance: float) -> float:
        pass

class CarStrategy(TravelStrategy):
    def travel_time(self, distance: float) -> float:
        speed = 60  # km/h
        return distance / speed

class BicycleStrategy(TravelStrategy):
    def travel_time(self, distance: float) -> float:
        speed = 15  # km/h
        return distance / speed

class WalkStrategy(TravelStrategy):
    def travel_time(self, distance: float) -> float:
        speed = 5  # km/h
        return distance / speed

class TravelContext:
    def __init__(self, strategy: TravelStrategy = None):
        self._strategy = strategy

    def set_strategy(self, strategy: TravelStrategy):
        self._strategy = strategy

    def calculate_time(self, distance: float) -> float:
        if not self._strategy:
            raise ValueError("A estratégia de transporte não foi definida.")
        return self._strategy.travel_time(distance)

def main():
    print("Escolha o meio de transporte:")
    print("1 - Carro")
    print("2 - Bicicleta")
    print("3 - A pé")

    choice = input("Digite o número correspondente ao meio de transporte: ")
    distance = float(input("Digite a distância em quilômetros: "))

    context = TravelContext()

    if choice == '1':
        context.set_strategy(CarStrategy())
    elif choice == '2':
        context.set_strategy(BicycleStrategy())
    elif choice == '3':
        context.set_strategy(WalkStrategy())
    else:
        print("Escolha inválida.")
        return

    time = context.calculate_time(distance)
    print(f"Tempo estimado de viagem: {time:.2f} horas")

if __name__ == "__main__":
    main()
