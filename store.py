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
			self.status = "Used"
			self.price*=0.8
		return self
	def displayall(self):
		print self.price
		print self.item_name
		print self.weight
		print self.brand
		print self.status
		return self

class Store(object):
	def __init__(self, location, owner):
		self.products = []
		self.location = location
		self.owner = owner
	def add_product(self, item_name):
		self.products.append(item_name)
		return self
	def remove_product(self, item_name):
		self.products.remove(item_name)
		return self
	def inventory(self): 
		#print self.products
		print self.location
		print self.owner 
		
print("\n")
product1 = Product(16, "Chips", "50oz", "Chetazz")
product1.returned("opened")
product1.tax()
product1.displayall()
print("\n")
product2 = Product(155, "Vine", "89oz", "Chateau Marmont")
product2.returned("in_the_box")
product2.tax()
product2.displayall()
print("\n")
store1 = Store("123 Lincoln St", "John Johnes")
store1.add_product(product1)
store1.add_product(product2)
store1.inventory()