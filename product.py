class Product(object):
	def __init__(self, price, item_name, weight, brand):
		self.price = price
		self.item_name = item_name
		self.weight = weight
		self.brand = brand
		self.status = "for sale"
	def sell(self):
		self.status = "sold"
		return self
	def tax(self):
		self.price*=1.1
		return self
	def returned(self, reason):
		if reason == "defective":
			self.status = "defective"
			self.price = 0 
		if reason == "in_the_box":
			self.status = "for sale"
		if reason == "opened":	
			self.status = "used"
			self.price*=0.8
		return self
	def displayall(self):
		print self.price
		print self.item_name
		print self.weight
		print self.brand
		print self.status
		
product1 = Product(16, "chips", 2, "Chetazz")
product1.returned("opened")
product1.tax()
product1.displayall()