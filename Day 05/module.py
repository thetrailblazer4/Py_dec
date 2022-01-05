prog_lang = ['Python', 'Java', 'C']

# find_index(prog_lang, 'Java')

def find_index(to_search, target):
	for index,value in enumerate(to_search):
		if value == target:
			return index

	return "No match"

print(find_index(prog_lang, 'java'))

# for i in prog_lang:
# 	print(i)


# for i,v in enumerate(prog_lang):
# 	if v == 'Java':
# 		print(i)
	# print(i, v)