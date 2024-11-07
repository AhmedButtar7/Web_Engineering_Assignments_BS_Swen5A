from abc import ABC, abstractmethod


class Payment(ABC):
	@abstractmethod
	def initatePayment(self):
		pass

	@abstractmethod
	def confirmPayment(self):
	    pass



class CreditCardPayment(Payment):

	def initatePayment(self,amount):
		print(f"Initiating credit card payment of {amount}")

	def confirmPayment(self):
		print("Credit Card Payment Cofirmed")



class PaypalPayment(Payment):
	def initatePayment(self,amount):
		print(f"Initiating Patpal payment of {amount}")

	def confirmPayment(self):
		print("Paymal Payment Cofirmed")


class PyamentProcessor:
	def processPayment(self,Payment,amount):
		Payment.initatePayment(amount)
		Payment.confirmPayment()





creditCardPayment = CreditCardPayment()
payPalPayment = PaypalPayment()
processor = PyamentProcessor()
# Process a credit card payment
processor.processPayment(creditCardPayment,100)
# Process Paypal Payment
processor.processPayment(payPalPayment,200)


