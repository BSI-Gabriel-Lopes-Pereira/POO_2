from abc import ABC, abstractmethod

class Produto(ABC):
    def __init__(self, cor):
        self.cor = cor
    
    def get_cor(self):
        return self.cor
    
    @abstractmethod
    def __str__(self):
        pass

class Poltrona(Produto):
    def __init__(self, cor, largura, altura, profundidade):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
        self.profundidade = profundidade
    
    def __str__(self):
        return f"Poltrona: {self.cor}, {self.largura}x{self.altura}x{self.profundidade}"

class MesaDeCentro(Produto):
    def __init__(self, cor, largura, altura, comprimento):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
        self.comprimento = comprimento
    
    def __str__(self):
        return f"Mesa de Centro: {self.cor}, {self.largura}x{self.altura}x{self.comprimento}"

class Sofa(Produto):
    def __init__(self, cor, largura, altura, profundidade):
        super().__init__(cor)
        self.largura = largura
        self.altura = altura
        self.profundidade = profundidade
    
    def __str__(self):
        return f"Sofá: {self.cor}, {self.largura}x{self.altura}x{self.profundidade}"

class FabricaDeMoveis(ABC):
    @abstractmethod
    def criar_poltrona(self):
        pass
    
    @abstractmethod
    def criar_mesa_de_centro(self):
        pass
    
    @abstractmethod
    def criar_sofa(self):
        pass

class FabricaMoveisModernos(FabricaDeMoveis):
    def criar_poltrona(self):
        return Poltrona("Cinza", 75, 85, 70)
    
    def criar_mesa_de_centro(self):
        return MesaDeCentro("Branco", 100, 40, 100)
    
    def criar_sofa(self):
        return Sofa("Preto", 200, 85, 90)

class FabricaMoveisRetro(FabricaDeMoveis):
    def criar_poltrona(self):
        return Poltrona("Vermelho", 70, 80, 65)
    
    def criar_mesa_de_centro(self):
        return MesaDeCentro("Madeira", 90, 45, 90)
    
    def criar_sofa(self):
        return Sofa("Azul", 190, 80, 85)

if __name__ == "__main__":
    fabrica_moderna = FabricaMoveisModernos()
    poltrona_moderna = fabrica_moderna.criar_poltrona()
    mesa_de_centro_moderna = fabrica_moderna.criar_mesa_de_centro()
    sofa_moderno = fabrica_moderna.criar_sofa()
    
    print(poltrona_moderna)
    print(mesa_de_centro_moderna)
    print(sofa_moderno)
    
    fabrica_retro = FabricaMoveisRetro()
    poltrona_retro = fabrica_retro.criar_poltrona()
    mesa_de_centro_retro = fabrica_retro.criar_mesa_de_centro()
    sofa_retro = fabrica_retro.criar_sofa()
    
    print(poltrona_retro)
    print(mesa_de_centro_retro)
    print(sofa_retro)
