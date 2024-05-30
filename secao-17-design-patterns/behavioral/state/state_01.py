"""
O Padrão de projeto State é um padrão comportamental
que tem a intenção de permitir a um objeto mudar
seu comportamento quando o seu estado interno
muda.
O objeto parecerá ter mudado sua classe.
"""

from __future__ import annotations
from abc import ABC, abstractmethod


class Order:
    """Context"""

    def __init__(self) -> None:
        self.state: OrderState = PaymentPending(self)

    def pending(self) -> None:
        print("Trying to execute pending()")
        self.state.pending()
        print(f"Status: {self.state}")

    def approve(self) -> None:
        print("Trying to execute approve()")
        self.state.approve()
        print(f"Status: {self.state}")

    def reject(self) -> None:
        print("Trying to execute reject()")
        self.state.reject()
        print(f"Status: {self.state}")


class OrderState(ABC):
    def __init__(self, order: Order) -> None:
        self.order = order

    @abstractmethod
    def pending(self) -> None:
        pass

    @abstractmethod
    def approve(self) -> None:
        pass

    @abstractmethod
    def reject(self) -> None:
        pass

    def __str__(self) -> str:
        return self.__class__.__name__


class PaymentPending(OrderState):
    def pending(self) -> None:
        print("Payment is already with status pending.")

    def approve(self) -> None:
        self.order.state = PaymentApproved(self.order)
        print("Payment approved.")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Payment rejected.")


class PaymentApproved(OrderState):
    def pending(self) -> None:
        self.order.state = PaymentPending(self.order)
        print("Payment pending.")

    def approve(self) -> None:
        print("Payment is already with status approved.")

    def reject(self) -> None:
        self.order.state = PaymentRejected(self.order)
        print("Payment rejected.")


class PaymentRejected(OrderState):
    def pending(self) -> None:
        print("Payment is already rejected, can't change the status.")

    def approve(self) -> None:
        print("Payment is already rejected, can't change the status.")

    def reject(self) -> None:
        print("Payment is already rejected, can't change the status.")


if __name__ == "__main__":
    order = Order()

    order.pending()
    print(f"\n{20 * '-'}\n")
    order.approve()
    print(f"\n{20 * '-'}\n")
    order.pending()
    print(f"\n{20 * '-'}\n")
    order.reject()
    print(f"\n{20 * '-'}\n")
    order.pending()
    print(f"\n{20 * '-'}\n")
    order.approve()
