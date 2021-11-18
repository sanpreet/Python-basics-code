import argparse


if __name__ == '__main__':
	
	parser = argparse.ArgumentParser()
	# optional arguments 
	parser.add_argument("--number1", help="first number")
	parser.add_argument("--number2", help="second number")
	parser.add_argument("--operation", help="operation", \
		choices=["add", "sub", "mul"])
	args =  parser.parse_args()

	# numbers will be returned in the string when passed from outside
	n1  = int(args.number1)
	n2 = int(args.number2)
	result = None
	
	if args.operation == 'add':
		result  = n1 + n2

	elif args.operation == 'sub':
		result  = n1 - n2

	elif args.operation == 'mul':
		result  = n1 * n2

	print("result is: {}".format(result))	
