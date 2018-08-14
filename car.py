class Car(object):
	def __init__(self, price, speed, fuel, mileage):
		self.price = price
		self.speed = speed
		self.fuel = fuel
		self.mileage = mileage
		if self.price > 10000:
			self.tax = 0.15
		else: 
			self.tax = 0.12
	def display_all(self):
		print "Price:", self.price
		print "Speed:", self.speed
		print "Fuel:", self.fuel
		print "Mileage:", self.mileage
		print "Tax:", self.tax
		return self
car1 = Car(2000, "35mph", "Full", "15mpg")
car2 = Car(600, "43mph", "King of Full", "36mpg")
car3 = Car(2000, "35mph", "Empty", "15mpg")
car4 = Car(1000, "40mph", "Full", "30mpg")
car5 = Car(20000, "20mph", "Not Full", "15mpg")
car6 = Car(6000000, "300mph", "Full", "5mpg")
car1.display_all()
print('')
car2.display_all()
print('')
car3.display_all()
print('')
car4.display_all()
print('')
car5.display_all()
print('')
car6.display_all()