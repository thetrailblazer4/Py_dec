# f = open('dem.log')
# print(f.read())
# f.close()

# print(f.closed)

'''
FileNotFoundError
NameError

'''

# try:
# 	pass
# except:
# 	pass
# else:
# 	pass
# finally:
# 	pass

try:
	f = open('dem.log')
	old_var = 'New Var'

except FileNotFoundError as e:
	print(e)

except NameError as e:
	print(e)

except Exception as e:
	print(e)

else:
	print(f.read())
	f.close()
	print(old_var)

finally:
	print("executing....")