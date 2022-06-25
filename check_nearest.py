class CheckNearest:
	
	def __init__(self,a,b):
		self.a = a
		self.b = b
		self.p = 1
		self.status=True
		self.lower_limit = False
		self.upper_limit = False

	def generate_up_low_limit(self):
		self.lower = 0
		self.upper = 0
		if self.a<=self.b:
			
			while self.status:
				if not self.lower_limit:
					self.temp = self.a**self.p
					if self.temp>=self.b:
						self.lower = self.a**(self.p-1)
						self.upper = self.a**(self.p)
						self.lower_limit = True
						self.upper_limit = True
						self.status = False
				self.p = self.p+1

		else:
			print("First value must be less than second value")
			return {}
		
		return {"a":self.a,"b":self.b,"lower":self.lower,"upper":self.upper}

	def get_nearest(self,data):
		self.low = data["b"]-data["lower"]
		self.up = data["upper"]-data["b"]
		if self.low==self.up:
			print("Both {} and {} are at equal distance to {}".format(data["lower"],data["upper"],data["b"]))
		elif self.low<self.up:
			print("{} is nearer to {}".format(data["lower"],data["b"]))
		else:
			print("{} is nearer to {}".format(data["upper"],data["b"]))
			
		

obj = CheckNearest(3,7)
data = obj.generate_up_low_limit()

if "lower" in data.keys():
	obj.get_nearest(data)
else:
	print("Invalid Data")			