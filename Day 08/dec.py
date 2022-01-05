# # def outer_func(message):
# # 	def inner_func():
# # 		print(message)

# # 	return inner_func

# # new_var = outer_func('hello')
# # # print(new_var.__name__)
# # new_var()


def decorator_func(func):
	def wrapper_func(*args):
		print('hello world!')
		print('Demo')
		return func(*args)
	return wrapper_func

@decorator_func
def display():
	print('This is a display func')

@decorator_func
def display_info(name, age):
	print(f'display_info ran with args({name}, {age})')

display_info('John', 26)

# # dec_disp = decorator_func(display)
# # dec_disp()

# # about_func = decorator_func(about)
# # about_func()

# # display()

# # def add(a, b):
# # 	return a + b

# # def sub(a, b):
# # 	return a - b


# # print(add(,4))


# def demo(*z):
# 	print(z)

# demo(1,2,3,3,45)