class Complex:
	def __init__(self,real,img):
		self.real= real
		self.img= img

	def add(self,c):
		self.real= self.real +c.real
		self.img= self.img + c.img
		return self

	def sub(self,c):
		self.real= self.real - c.real
		self.img= self.img - c.img
		return self

	def mod(self):
		sqrt=((self.real)**2 + (self.img)**2)**0.5
		return sqrt

	def mul(self, c):
		self.real= (self.real)*(c.real) - (self.img)*(c.img)
		self.img= (self.real)*(c.img) + (self.img)*(c.real)
		return self

	def conjugate(self):
		self.real=self.real
		self.img= - self.img
		return self

	def inverse(self):
		self.real= (self.real)/(self.conjugate())**2
		self.img= -(self.img)/(self.conjugate())**2
		return self

	def display(self):
		if self.img>0:
			print(str(self.real), '+', str(self.img)+'i')

		else:
			print(str(self.real), str(self.img)+'i')


a=Complex(1,2)
a.display()
b=Complex(2,-3)
c=complex(0,0)
c=b.add(a)
c.display()
c.conjugate().display()
