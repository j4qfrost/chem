class Molecule:
	def __init__(self,name,formula,mass):
		super(,self).__init__()
		self.name = name
		self.formula = formula
		self.mass = mass

class Element:
	def __init__(self,name,symbol,number,mass,group,period):
		super(Element,self).__init__()
		self.name = name
		self.symbol = symbol
		self.number = number
		self.mass = mass
		self.group = group
		self.period = period
		
	def __add__(self,other):
		return Molecule(self.name + " " + other.name, self.symbol + other.symbol, self.mass + other.mass)