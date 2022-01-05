class Emp:

	raise_amt = 1.04
	num_of_emps = 0

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f"{first}.{last}@company.com"
		self.pay = pay

		Emp.num_of_emps += 1

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)


print(Emp.num_of_emps)

emp_1 = Emp('John', 'K', 500.30)
emp_2 = Emp('jane', 'M', 60000)

print(Emp.num_of_emps)

# Emp.raise_amt = 2.03
# emp_1.raise_amt = 1.05

# print(Emp.raise_amt)

# print(emp_1.pay)
# emp_1.apply_raise()
# print(emp_1.pay)

# print(Emp.raise_amt)
# print(emp_1.raise_amt)
# print(emp_2.raise_amt)

