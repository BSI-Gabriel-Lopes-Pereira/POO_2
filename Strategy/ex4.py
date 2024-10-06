# Implemente um jogo simples onde diferentes personagens podem atacar usando estratégias de
# ataque variadas (por exemplo, ataque corpo a corpo, ataque à distância, ataque mágico).

from abc import ABC, abstractmethod

class EstrategiaDeAtaque(ABC):
    @abstractmethod
    def atacar(self):
        pass

class AtaqueCorpoACorpo(EstrategiaDeAtaque):
    def atacar(self):
        return "Ataque corpo a corpo!"

class AtaqueDistancia(EstrategiaDeAtaque):
    def atacar(self):
        return "Ataque à distância!"

class AtaqueMagico(EstrategiaDeAtaque):
    def atacar(self):
        return "Ataque mágico!"

class Personagem:
    def __init__(self, nome: str, estrategia: EstrategiaDeAtaque = None):
        self.nome = nome
        self.estrategia = estrategia

    def set_estrategia(self, estrategia: EstrategiaDeAtaque):
        self.estrategia = estrategia

    def atacar(self):
        if self.estrategia:
            print(f"{self.nome} usa: {self.estrategia.atacar()}")
        else:
            print(f"{self.nome} não tem uma estratégia de ataque definida.")

def main():
    guerreiro = Personagem("Guerreiro", AtaqueCorpoACorpo())
    arqueiro = Personagem("Arqueiro", AtaqueDistancia())
    mago = Personagem("Mago", AtaqueMagico())

    guerreiro.atacar()
    arqueiro.atacar()
    mago.atacar()

    print("\nMudando a estratégia de ataque do Guerreiro para ataque à distância.")
    guerreiro.set_estrategia(AtaqueDistancia())
    guerreiro.atacar()

if __name__ == "__main__":
    main()
