class Bike(object):
	def __init__(self, price, max_speed):
		self.price = price
		self.miles = 0
		self.max_speed = max_speed
	def displayinfo(self):
		print self.price
		print self.max_speed
		print self.miles
		return self
	def ride(self):
		print "Riding"
		self.miles += 10
		print self.miles
		return self
	def reverse(self):
		if self.miles <= 0:
			print "Can't reverse"
			return self
		elif self.miles >= 0:
			self.miles -= 5
			print self.miles 
			print "Reversing"
			return self

bike1 = Bike(200, "25mph")
bike1.ride().ride().ride().reverse().displayinfo()
bike1.ride().ride().reverse().reverse().displayinfo()
bike1.reverse().reverse().reverse().displayinfo()