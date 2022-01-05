class Emp:

	raise_amt = 1.04

	def __init__(self, first, last, pay):
		self.first = first
		self.last = last
		self.email = f"{first}.{last}@company.com"
		self.pay = pay

	def fullname(self):
		return f"{self.first} {self.last}"

	def apply_raise(self):
		self.pay = int(self.pay * self.raise_amt)

class Dev(Emp):
	raise_amt = 1.10

	def __init__(self, first, last, pay, prog_lang):
		# Emp.__init__(self, first, last, pay)
		super().__init__(first, last, pay)
		self.prog_lang = prog_lang

class Mgr(Emp):
	
	def __init__(self, first, last, pay, emps=None):
		super().__init__(first, last, pay)

		if emps is None:
			self.emps = []
		else:
			self.emps = emps

	def add_emp(self, emp):
		if emp not in self.emps:
			self.emps.append(emp)

	def remove_emp(self, emp):
		if emp in self.emps:
			self.emps.remove(emp)

	def show_emps(self):
		for emp in self.emps:
			print('--->', emp.fullname())
	

emp_1 = Dev('John', 'K', 500.30, 'Python')
emp_2 = Emp('jane', 'M', 60000)
mgr_1 = Mgr('Tom', 'K', 90000)

mgr_1.add_emp(emp_1)
mgr_1.add_emp(emp_2)

mgr_1.remove_emp(emp_1)
# mgr_1.show_emps()


print(isinstance(mgr_1, Emp))

print(issubclass(Mgr, Dev))
# print(help(Mgr))

# print(emp_1.prog_lang)
