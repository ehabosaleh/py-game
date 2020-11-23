class Employee:
	raise_amount=12
	def printraise(self):
		print(self.raise_amount)

x=Employee()
print(x.raise_amount)
print(Employee.raise_amount)
x.printraise()
print(x.__dict__)
