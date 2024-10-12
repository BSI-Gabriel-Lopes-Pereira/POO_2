from abc import ABC, abstractmethod

class IObserver(ABC):
    @abstractmethod
    def update(self, news: str):
        pass

class IObservable(ABC):
    @abstractmethod
    def subscribe(self, observer: IObserver):
        pass

    @abstractmethod
    def unsubscribe(self, observer: IObserver):
        pass

    @abstractmethod
    def notify(self):
        pass

class Reuters(IObservable):
    def __init__(self):
        self._observers = []
        self._news = ""

    def subscribe(self, observer: IObserver):
        self._observers.append(observer)

    def unsubscribe(self, observer: IObserver):
        self._observers.remove(observer)

    def set_news(self, news: str):
        self._news = news
        self.notify()

    def notify(self):
        for observer in self._observers:
            observer.update(self._news)

class NewsChannel(IObserver):
    def __init__(self, name: str):
        self._name = name

    def update(self, news: str):
        print(f"Transmissão {self._name}: {news}")

if __name__ == "__main__":
    reuters = Reuters()

    cnn = NewsChannel("CNN")
    fox_news = NewsChannel("Fox News")
    bbc = NewsChannel("BBC")

    reuters.subscribe(cnn)
    reuters.subscribe(fox_news)
    reuters.subscribe(bbc)

    reuters.set_news("Notícia de última hora: Grande tempestade se aproximando da costa!")

    reuters.unsubscribe(fox_news)

    reuters.set_news("Notícia de última hora: Mercado de ações vê crescimento sem precedentes!")
