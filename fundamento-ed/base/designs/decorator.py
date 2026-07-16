from abc import ABC, abstractmethod

class Notificador(ABC):
    """Interface base para todos os notificadores"""
    @abstractmethod
    def enviar(self, mensagem: str) -> str:
        pass

class NotificadorEmail(Notificador):
    """Implementação concreta do notificador básico (email)"""
    def enviar(self, mensagem: str) -> str:
        return f"Email enviado: {mensagem}"

class NotificadorSMS(Notificador):
    """Implementação concreta alternativa"""
    def enviar(self, mensagem: str) -> str:
        return f"SMS enviado: {mensagem}"

class NotificadorDecorator(Notificador):
    """Classe base para todos os decorators"""
    def __init__(self, notificador: Notificador):
        self._notificador = notificador

    @abstractmethod
    def enviar(self, mensagem: str) -> str:
        return self._notificador.enviar(mensagem)

class DecoratorCriptografia(NotificadorDecorator):
    """Adiciona criptografia à mensagem"""
    def enviar(self, mensagem: str) -> str:
        mensagem_cripto = f"[CRIPTOGRAFADA] {mensagem} [CRIPTOGRAFADA]"
        return self._notificador.enviar(mensagem_cripto)

class DecoratorLog(NotificadorDecorator):
    """Adiciona registro de log"""
    def enviar(self, mensagem: str) -> str:
        print(f"LOG: Tentativa de envio - {mensagem[:20]}...")
        resultado = self._notificador.enviar(mensagem)
        print(f"LOG: Envio concluído")
        return resultado

class DecoratorFormatacaoHTML(NotificadorDecorator):
    """Adiciona formatação HTML"""
    def enviar(self, mensagem: str) -> str:
        mensagem_html = f"<html><body>{mensagem}</body></html>"
        return self._notificador.enviar(mensagem_html)

# Notificador básico
notificador_simples = NotificadorEmail()
print(notificador_simples.enviar("Olá, mundo!"))
# Saída: Email enviado: Olá, mundo!

# Decorado com múltiplas funcionalidades
notificador_avancado = DecoratorLog(
    DecoratorCriptografia(
        DecoratorFormatacaoHTML(
            NotificadorSMS()
        )
    )
)
resultado = notificador_avancado.enviar("Mensagem importante!")
print(resultado)


"""
Saída:
LOG: Tentativa de envio - Mensagem importante!...
LOG: Envio concluído
SMS enviado: <html><body>[CRIPTOGRAFADA] Mensagem importante! [CRIPTOGRAFADA]</body></html>
"""