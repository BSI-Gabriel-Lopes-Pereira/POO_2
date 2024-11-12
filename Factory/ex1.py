from abc import ABC, abstractmethod

class VeiculoMotorizado(ABC):
    @abstractmethod
    def construir(self):
        pass

class Moto(VeiculoMotorizado):
    def construir(self):
        print("Construindo uma moto.")

class Carro(VeiculoMotorizado):
    def construir(self):
        print("Construindo um carro.")

class FabricaVeiculoMotorizado(ABC):
    def criar(self):
        veiculo = self.criar_veiculo_motorizado()
        veiculo.construir()
        return veiculo
    
    @abstractmethod
    def criar_veiculo_motorizado(self):
        pass

class FabricaMoto(FabricaVeiculoMotorizado):
    def criar_veiculo_motorizado(self):
        return Moto()

class FabricaCarro(FabricaVeiculoMotorizado):
    def criar_veiculo_motorizado(self):
        return Carro()

if __name__ == "__main__":
    fabrica_moto = FabricaMoto()
    moto = fabrica_moto.criar()

    fabrica_carro = FabricaCarro()
    carro = fabrica_carro.criar()
