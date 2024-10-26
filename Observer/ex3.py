class Notificador:
    def enviar(self, mensagem):
        raise NotImplementedError("Método enviar() deve ser implementado")

class NotificadorPadrão(Notificador):
    def enviar(self, mensagem):
        print(f"Enviando notificação padrão: {mensagem}")

class NotificadorDecorator(Notificador):
    def __init__(self, notificador):
        self._notificador = notificador

    def enviar(self, mensagem):
        self._notificador.enviar(mensagem)

class NotificadorEmail(NotificadorDecorator):
    def enviar(self, mensagem):
        super().enviar(mensagem)
        print(f"Enviando email: {mensagem}")

class NotificadorSMS(NotificadorDecorator):
    def enviar(self, mensagem):
        super().enviar(mensagem)
        print(f"Enviando SMS: {mensagem}")

class NotificadorSlack(NotificadorDecorator):
    def enviar(self, mensagem):
        super().enviar(mensagem)
        print(f"Enviando Slack: {mensagem}")

notificador = NotificadorPadrão()

notificador = NotificadorEmail(notificador)
notificador = NotificadorSMS(notificador)
notificador = NotificadorSlack(notificador)

notificador.enviar("Hello World!")
