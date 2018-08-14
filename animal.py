class Animal(object):
	def __init__(self, name, health):
		self.name = name
		self.health = health
		print self.name
	def walk(self):
		self.health -= 1
		return self
	def run(self):
		self.health -= 5
		return self
	def display_health(self):
		print self.health
class Dog(Animal):
	def __init__(self, name):
		super(Dog, self).__init__(name, 150)
		#print self.name
	def pet(self):
		self.health += 5
		return self
class Dragon(Animal):
	def __init__(self, name):
		super(Dragon, self).__init__(name, 170)
	def fly(self):
		self.health -= 10
		return self
	def display_health(self):
		print self.health
		print "I am a Dragon"	

print("\n")
dragon1 = Dragon("Droch")
dragon1.fly().fly().fly().display_health()
print("\n")
animal1 = Animal("Zeb", 100)	
animal1.walk().walk().walk().run().run().display_health()
print("\n")
dog1 = Dog("Gibbs")
dog1.walk().walk().walk().run().run().pet().display_health()