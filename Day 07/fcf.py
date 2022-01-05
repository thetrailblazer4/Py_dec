# Decorators<--- Closures <<< First Class Functions

'''
A programming language is said to have First-class functions 
when functions in that language are treated like any other variable. 

For example, in such a language, 
a function can be passed as an argument to other functions, 
can be returned by another function and 
can be assigned as a value to a variable.
'''

# def sqaure(x):
# 	return x * x

# # def cube(x):
# # 	return x * x * x

# result = sqaure
# print(result(8))
# # [1,2,3,4] ---> [1,4,9,16]

# # for i in [1,2,3,4]:
# # 	print(i*i)
# def my_sq(func, lst):
# 	result = []
# 	for i in lst:
# 		result.append(func(i))
# 	return result

# print(my_sq(sqaure, [1,2,3,4]))
# print(my_sq(cube, [1,2,3,4]))




def outer_func(message):
	def inner_func():
		print(message)

	return inner_func

new_var = outer_func('hello')
# print(new_var.__name__)
new_var()