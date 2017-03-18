#!/usr/bin/env python3

import operator

OPERATORS = {
	'+': operator.add,
	'-': operator.sub,
}


def calculate(arg):
	pass


def main():
	while True:
		result = calculate(input('rpn calc> '))
		print("Result:", result)


if __name__ == '__main__':
	main()
