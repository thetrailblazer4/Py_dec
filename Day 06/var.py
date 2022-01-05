# LEGB -> Local --> Enclosing --> Global --> Builtins

# x = 'global x'


# def demo(z):
# 	x = 'local y'
# 	print(z)

# demo('Hello')
# print(x)
# # print(z)


# def max():
# 	pass

# num = [5,1,2,4,3]

# m = max(num)
# print(m)

x = 'global x'

def outer():
	x = 'outer x'

	def inner():
		x = 'inner x'
		print(x)
	inner()

	print(x)

outer()
# print(x)
