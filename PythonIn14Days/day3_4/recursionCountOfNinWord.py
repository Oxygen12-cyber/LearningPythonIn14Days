def main():
	number = int(input('your character: '))
	counts = count_digits(number)
	print(f'the number {number} has {counts} characters ')
	
def count_digits(digit):
	if digit == 0:
		return 0
	else:
		return 1 + count_digits(digit // 10)
			
			
main()