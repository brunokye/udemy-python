"""
Polimorfismo é o princípio que permite que
classes deridavas de uma mesma superclasse
tenham métodos iguais (com mesma assinatura)
mas comportamentos diferentes.

Assinatura do método = Mesmo nome e quantidade
de parâmetros (retorno não faz parte da assinatura)
Opinião + princípios que contam:
Assinatura do método: nome, parâmetros e retorno iguais

Princípio da substituição de liskov
Objetos de uma superclasse devem ser substituíveis
por objetos de uma subclasse sem quebrar a aplicação.

Sobrecarga de métodos (overload)  🐍 = ❌
Sobreposição de métodos (override) 🐍 = ✅
"""

from abc import ABC, abstractmethod


class Notification(ABC):
    def __init__(self, msg):
        self._msg = msg

    @abstractmethod
    def enviar(self):
        ...


class EmailNotification(Notification):
    def enviar(self) -> bool:
        print(f"E-mail: enviando - {self._msg}")
        return True


class SMSNotification(Notification):
    def enviar(self) -> bool:
        print(f"SMS: enviando - {self._msg}")
        return False


def notify(notification: Notification):
    sent = notification.enviar()

    if sent:
        print("Notificação enviada.")
    else:
        print("Notificação não enviada.")


email = notify(EmailNotification("Teste Email"))
sms = notify(SMSNotification("Teste SMS"))
