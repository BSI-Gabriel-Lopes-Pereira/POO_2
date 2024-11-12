from abc import ABC, abstractmethod

class Transporte(ABC):
    @abstractmethod
    def entregar(self):
        pass

class Caminhao(Transporte):
    def entregar(self):
        print("Entrega realizada por Caminhão.")

class Navio(Transporte):
    def entregar(self):
        print("Entrega realizada por Navio.")

class Aviao(Transporte):
    def entregar(self):
        print("Entrega realizada por Avião.")

class FabricaTransporte(ABC):
    @abstractmethod
    def criar_transporte(self):
        pass

class FabricaCaminhao(FabricaTransporte):
    def criar_transporte(self):
        return Caminhao()

class FabricaNavio(FabricaTransporte):
    def criar_transporte(self):
        return Navio()

class FabricaAviao(FabricaTransporte):
    def criar_transporte(self):
        return Aviao()

if __name__ == "__main__":
    fabrica_transporte = FabricaCaminhao()
    transporte = fabrica_transporte.criar_transporte()
    transporte.entregar()

    fabrica_transporte = FabricaNavio()
    transporte = fabrica_transporte.criar_transporte()
    transporte.entregar()

    fabrica_transporte = FabricaAviao()
    transporte = fabrica_transporte.criar_transporte()
    transporte.entregar()
