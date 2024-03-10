
def test_print():
	print("Python Toolkit")

def indent(spaces):
	indent = ' ' * spaces
	return indent

def dict_navigation(dictionary):
	for x in dictionary.keys():
		print(f'{indent(4)}{x}')
	user_input = input()
	if user_input in dictionary:
		sub_dict = dictionary[user_input]
		for y in sub_dict:
			print(f'{indent(4)}{y}: {sub_dict[y]}')
	else:
		print('Data Type does not exist')

def data_type_library():
	data_type_dict = {
		'integer': {
			'Class': 'int', 
			'Category':'numerics',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		'float': {
			'Class': 'float', 
			'Category':'numerics',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		'boolean': {
			'Class': 'bool', 
			'Category':'booleans',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		'string': {
			'Class': 'str', 
			'Category':'text sequences',
			'Kind': 'primative',
			'Mutable': 'No'
			},
		}

	print('See below for all data types. Type the name of one to see details')
	dict_navigation(data_type_dict)

def collections_library():
	collections_dict = {
		'range': {
			'Class': 'range', 
			'Category':'sequences - homogeneous',
			'Kind': 'non-primative',
			'Mutable': 'No',
			'example': 'my_range = '
		},
		'tuples': {
			'Class': 'range', 
			'Category':'sequences - heterogeneous',
			'Kind': 'non-primative',
			'Mutable': 'No',
			'example': 'my_tuple = (any data type)'
		},
		'lists': {
			'Class': 'range', 
			'Category':'sequences - heterogeneous',
			'Kind': 'non-primative',
			'Mutable': 'Yes',
			'example': 'my_list = [any data type]'
		},
		'dictionaries': {
			'Class': 'dict', 
			'Category':'maps',
			'Kind': 'non-primative',
			'Mutable': 'Yes',
			'example': 'my_dict = {key:value, key:value}'
		},
		'sets': {
			'Class': 'set', 
			'Category':'set',
			'Kind': 'non-primative',
			'Mutable': 'Yes',
			'example': 'my_set = {any data type}'
		},
		'frozen sets': {
			'Class': 'frozenset', 
			'Category':'set',
			'Kind': 'non-primative',
			'Mutable': 'No',
			'example': 'my_set = {any data type}'+f'\n{indent(13)}frozen_set = frozenset(my_set)'
		},
	}
	print('See below for all collection types. Type the name of one to see details')
	dict_navigation(collections_dict)

	def loop_library():
		library_dict = {
			'while loops': 'example',
			'for loops': 'example',
			'comprehensions': {
				'list comprehensions': 'example',
				'dict comprehensions': 'example',
			},
		}

	print('See below for all collection types. Type the name of one to see details')
	dict_navigation(library_dict)
