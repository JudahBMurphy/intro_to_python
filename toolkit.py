# This program serves as a quick reference guide to basic commands 
# and syntax learned so far. Intended to be accessed using Terminal

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

#def python_help():

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
			print('Accessing Terminal guide:')
			main_menu_loop_control = True
			cmd_ln_help()
		case 2:
			print('Accessing Git guide:')
			main_menu_loop_control = True
			git_help()
		case 3:
			print('Accessing Python guide:')
			main_menu_loop_control = True
		case _:
			print('Command not recognized. Try again using specified options.')
			help_input = int(input())
