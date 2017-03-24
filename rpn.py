#!/usr/bin/env python3

import operator
from termcolor import colored

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
	'*': operator.mul,
	'/': operator.truediv,
	'^': operator.pow,
	'%': operator.mod,
	'|': operator.or_
}


def calculate(arg):
	stack = list()
	for operand in arg.split():
		try:
			operand = float(operand)
			stack.append(operand)
		except:
			arg2 = stack.pop()
			arg1 = stack.pop()
			operator_fn = OPERATORS[operand]
			result = operator_fn(arg1, arg2)
			
			stack.append(result)
	return stack.pop()

def main():
	while True:
		prompt = colored('rpn calc> ', 'green', attrs=['underline'])
		result = calculate(input(prompt))
		if result < 0:
			result = colored(result, 'red', attrs=['bold'])
		if result == 100:
			result = colored(result, 'yellow', attrs=['blink'])
		print("Result:", result)

if __name__ == '__main__':
	main()
