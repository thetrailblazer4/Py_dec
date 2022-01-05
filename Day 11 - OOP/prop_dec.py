class Emp:

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		# self.email = f"{first}.{last}@company.com"
		self.pay = pay

	@property
	def email(self):
		return f"{self.first}.{self.last}@company.com"

	@property
	def fullname(self):
		return f"{self.first} {self.last}"



emp_1 = Emp('John', 'K', 500.30)

emp_1.first = 'Jane'

print(emp_1.first)
print(emp_1.last)
print(emp_1.fullname)
print(emp_1.email)