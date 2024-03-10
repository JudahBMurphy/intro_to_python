# This program serves as a quick reference guide to basic commands 
# and syntax learned so far. Intended to be accessed using Terminal.

import toolkit_python

def cmd_ln_help():
	print('''See following list of Terminal Commands:
Note: 'x' indicates name of file or directory. 'y' indicates a path.
	man x - Display documentation about a command.
	cd x - Change directory
	ls - List files and directories in current directory.
	pwd - Display the path of the current directory.
	touch x - Create a file.
	mkdir x - Create a directory
	rm x - Remove a file. Use 'rm -r' to remove a directory.
	cp x - Copy a file or directory.
	mv x y - Move or rename a file or directory.
	echo - Print text to STDOUT.
	cat x - Display contents of a file.
	more x - Display contents of a file. Lets the user scroll down.
	less x - Display contents of a file in an even more interactive way.
	head x - Display the first part of a file.
	tail x - Display the last part of a file.
	''')

def git_help():
	print('''See following list of Git commands:
Note: 'x' indicates name of file or directory. 'y' indicates a path.
	git init - Creates git repository in current directory. 
	git status - Display status of files in git repository
	git add x - Stages file for the next commit
	git commit - Commits staged files to the repository
	git log - Display the commit history
	''')

def python_menu_loop():
	print('''What do you need assistence with?
Choose from list by typing in corresponding number:
	1. Data Types
	2. Collections
	3. Loops
	4. Functions and Methods
	5. Concepts
	6. Documentation''')
	loop_controller = False
	python_help_input = int(input())
	while loop_controller != True:
		match python_help_input:
			case 1:
				loop_controller = True
				toolkit_python.data_type_library()
			case 2:
				loop_controller = True
				toolkit_python.collections_library()
			case _:
				print('Command not recognized. Try again using specified options.')
				python_help_input = int(input())

print('''What do you need?
Choose from list by typing in corresponding number:
	1. Help with Terminal
	2. Help with Git
	3. Help with Python''')
help_input = int(input())
main_menu_loop_control = False

while main_menu_loop_control != True:
	match help_input:
		case 1:
			main_menu_loop_control = True
			cmd_ln_help()
		case 2:
			main_menu_loop_control = True
			git_help()
		case 3:
			python_menu_loop()
			main_menu_loop_control = True
		case _:
			print('Command not recognized. Try again using specified options.')
			help_input = int(input())
