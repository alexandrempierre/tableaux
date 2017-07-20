#!/usr/bin/env python3

from tableaux import *
from nltk import *

read_expr = Expression.fromstring

def input_func(file=False,read=read_expr,input_msg=None):
	if input_msg is None:
		input_msg = ''

	read_file_line = lambda: read(file.readline().strip())
	read_input = lambda: read(input(input_msg).strip())

	while True:
		try:
			if file:
				return read_file_line()

			return read_input()
		except ValueError:
			print('Press Ctrl+C to close the program')
			continue
		except KeyboardInterrupt:
			print('\n\nProgram closed by the user...\n')
			exit()

def get_qt_problems(file=False):
	return input_func(file=file, read=int, \
		input_msg='Number of tableauxs to solve: ')

def get_goal(file=False):
	return input_func(file=file, read=read_expr, \
		input_msg='Affirmation to deduce: ')

def get_assumptions(file=False):
	number = input_func(file=file, read=int, \
		input_msg='Number of assumptions given: ')

	assumptions = []
	for i in range(1,number+1):
		assumptions.append(input_func(file=file, read=read_expr, \
			input_msg='Assumption {0}/{1}: '.format(i, number)))

	return assumptions

def get_problem(file=False):
	goal = get_goal(file)
	assumptions = get_assumptions(file)

	if file:
		print('Goal: {0}'.format(goal))
		print('Assumptions:\n')
		for assumption in assumptions:
			print(assumption)

	return goal,assumptions

def problems(file=False):
	qt_problems = get_qt_problems(file)

	for i in range(1,qt_problems+1):
		print("\n===================== Problem {0}/{1} =====================\n".format(i, qt_problems))
		goal, assumptions = get_problem(file)
		if tableaux(goal, assumptions):
			print("\nThis tableaux is closed")
		else:
			print("\nThis tableaux can't be closed")

	print("\nNo more problems to solve\nClosing...\n")

if __name__ == '__main__':
	from sys import argv

	if len(argv) == 1:
		problems()
	else:
		file_name = argv[1]
		try:
			with open(file_name) as f:
				problems(f)
		except FileNotFoundError:
			ans = input('File not found, want to manually enter the necessary data? (yes/[no]) ')
			if ans.strip() in ['yes', 'sim', 'y', 's', 'prox', 'proximo', 'next', 'p', '1']:
				problems()
			else:
				print('See ya!')
