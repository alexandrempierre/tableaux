#!/usr/bin/env python3

from tableaux import *
from nltk import *

read_expr = Expression.fromstring

def manual_input_indiv_tab():
	assumptions = []

	goal = read_expr(input('Affirmation to deduce: '))
	num_assumptions = int(input('Number of assumptions given: '))

	for i in range(1,num_assumptions+1):
		assumptions.append(read_expr(input('Assumption {0}/{1}: '.format(i,num_assumptions))))
	return goal,assumptions

def manual_input_all():
	problems = int(input('Number of tableauxs to solve: '))
	for i in range(problems):
		goal,assumptions = manual_input_indiv_tab()

		print(tableaux(goal=goal, assumptions=assumptions))

if __name__ == '__main__':
	from sys import argv

	if len(argv) == 1:
		manual_input_all()
	else:
		file_name = argv[1]

		try:
			with open(file_name) as f:
				problems = int(f.readline().strip())
				for i in range(problems):
					goal = f.readline().strip()
					while goal == '':
						goal = f.readline().strip()
					goal = read_expr(goal)
					num_assumptions = int(f.readline().strip())
					assumptions = []
					for i in range(1,num_assumptions+1):
						assumptions.append(read_expr(f.readline().strip()))
					print(tableaux(goal=goal, assumptions=assumptions))
		except FileNotFoundError:
			ans = input('File not found, want to manually enter the necessary data? (yes/[no]) ')
			if (ans or 'no').lower() not in ['no','dont',"don't",'not','0','false']:
				manual_input_all()
			else:
				print('See ya!')
