from abc import ABC, abstractmethod


# Strategy Interface
class PaymentStrategy(ABC):

    @abstractmethod
    def pay(self, amount):
        pass


# Credit Card Payment
class CreditCard(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} paid using Credit Card.")


# PayPal Payment
class PayPal(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} paid using PayPal.")


# UPI Payment
class UPI(PaymentStrategy):

    def pay(self, amount):
        print(f"₹{amount} paid using UPI.")


# Context Class
class PaymentProcessor:

    def __init__(self, payment_method):
        self.payment_method = payment_method

    def process_payment(self, amount):
        self.payment_method.pay(amount)


# Main Program
amount = float(input("Enter Amount: ₹"))

print("\nChoose Payment Method")
print("1. Credit Card")
print("2. PayPal")
print("3. UPI")

choice = input("Enter Choice: ")

if choice == "1":
    payment = CreditCard()
elif choice == "2":
    payment = PayPal()
elif choice == "3":
    payment = UPI()
else:
    print("Invalid Choice")
    exit()

processor = PaymentProcessor(payment)
processor.process_payment(amount)



Enter Amount: ₹500

Choose Payment Method
1. Credit Card
2. PayPal
3. UPI
Enter Choice: 3
₹500.0 paid using UPI.

