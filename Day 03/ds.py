# Mutable

# list_1 = ['Maths', 'Physics', 'CompSci', 'History']

# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Bio'

# print(list_1)
# print(list_2)

#tuple - Immutable

# list_1 = ('Maths', 'Physics', 'CompSci', 'History')

# list_2 = list_1

# print(list_1)
# print(list_2)

# list_1[0] = 'Bio'

# print(list_1)
# print(list_2)


# courses = {'Maths', 'Physics', 'CompSci', 'History', 'Maths', 'CompSci'}

# print('CompSci' in courses)

# print(courses)

# Empty_lists
# empty_list = []
# empty_list = list()

# # Empty_tuples
# empty_tuple = ()
# empty_tuple = tuple()

# # Empty_sets
# empty_set = {}  #<- This is used for creating dict
# empty_set = set()


# Dict - Key: value -- Mappings

# emp = {'id':1, 'name':'John', 'prog_lang':['Python', 'JS']}


# for keys, values in emp.items():
# 	print(f"{keys} - {values}")

# emp['phone'] = '444-44444'
# emp['email'] = 'john.k@company.com'

# emp.update({'name':['jane', 'Tom'], 'phone': '4444-4444', 'email':'jane@comp.com'})


# print(emp['name'][0])

# del emp['id']
# removed = emp.pop('id')

# print(emp)
# print(removed)

# print(emp.keys())
# print(emp.values())
# print(emp.items())
