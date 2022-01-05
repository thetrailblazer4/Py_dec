



import datetime
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

	@classmethod
	def set_raise_amt(cls, amount):
		cls.raise_amt = amount

	@classmethod
	def from_str(cls, emp_str):
		first, last, pay = emp_str.split('-')
		return cls(first, last, pay)

	@staticmethod
	def is_workday(day):
		
		if day.weekday() == 5 or day.weekday() ==6:
			return False
		return True


	def __repr__(self):
		return f"Emp('{self.first}', '{self.last}', {self.pay})"

	def __str__(self):
		return f"{self.fullname()}, {self.email}"

emp_1 = Emp('John', 'K', 500.30)
emp_2 = Emp('jane', 'M', 60000)

print(repr(emp_1))
print(str(emp_1))

print(emp_1)


# my_date = datetime.date(2021,12,26)

# print(Emp.is_workday(my_date))

# emp_1_str = 'John-K-500.30'

# new_emp = Emp.from_str(emp_1_str)

# # first, last, pay = emp_1_str.split('-')
# # new_emp = Emp(first, last, pay)

# print(new_emp.first)





# # Emp.set_raise_amt(1.05)

# # print(Emp.raise_amt)
# # print(emp_1.raise_amt)
# # print(emp_2.raise_amt)



# import datetime

# print(datetime.__file__)