from abc import ABC, abstractmethod

class Relatorio(ABC):
    @abstractmethod
    def gerar(self, dados):
        pass

class RelatorioHTML(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório em HTML com dados: {dados}")

class RelatorioCSV(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório em CSV com dados: {dados}")

class RelatorioJSON(Relatorio):
    def gerar(self, dados):
        print(f"Gerando relatório em JSON com dados: {dados}")

class FabricaRelatorio(ABC):
    @abstractmethod
    def criar_relatorio(self):
        pass

class FabricaRelatorioHTML(FabricaRelatorio):
    def criar_relatorio(self):
        return RelatorioHTML()

class FabricaRelatorioCSV(FabricaRelatorio):
    def criar_relatorio(self):
        return RelatorioCSV()

class FabricaRelatorioJSON(FabricaRelatorio):
    def criar_relatorio(self):
        return RelatorioJSON()

if __name__ == "__main__":
    dados = {"nome": "João", "idade": 30}

    fabrica_relatorio = FabricaRelatorioHTML()
    relatorio = fabrica_relatorio.criar_relatorio()
    relatorio.gerar(dados)

    fabrica_relatorio = FabricaRelatorioCSV()
    relatorio = fabrica_relatorio.criar_relatorio()
    relatorio.gerar(dados)

    fabrica_relatorio = FabricaRelatorioJSON()
    relatorio = fabrica_relatorio.criar_relatorio()
    relatorio.gerar(dados)
