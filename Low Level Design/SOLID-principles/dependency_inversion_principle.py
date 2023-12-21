# this principle states that - 
# Abstractions should not depend upon details. Details should depend upon abstractions.

from abc import ABC, abstractmethod

class PaymentGateway(ABC):
    @abstractmethod
    def pay(self, amount: float) -> bool:
        pass

class PayPal(PaymentGateway):
    def pay(self, amount: float) -> bool:
        print(f'Paying {amount} using PayPal')
        return True

class Stripe(PaymentGateway):
    def pay(self, amount: float) -> bool:
        print(f'Paying {amount} using Stripe')
        return True

class PaymentProcessor:
    def __init__(self, payment_gateway: PaymentGateway):
        self.payment_gateway = payment_gateway

    def process_payment(self, amount: float) -> bool:
        return self.payment_gateway.pay(amount)

if __name__ == '__main__':
    paypal = PayPal()
    stripe = Stripe()

    payment_processor = PaymentProcessor(paypal)
    payment_processor.process_payment(100)

    payment_processor = PaymentProcessor(stripe)
    payment_processor.process_payment(100)


# If you want to use a different payment gateway, you’ll need to change the PaymentProcessor class. 
# To prevent this, you need to invert the dependency so that the PayPal and Stripe classes need to adapt to the PaymentProcessor class. 
# To do that, you define an interface and make the PaymentProcessor dependent on it instead of PayPal and Stripe classes
