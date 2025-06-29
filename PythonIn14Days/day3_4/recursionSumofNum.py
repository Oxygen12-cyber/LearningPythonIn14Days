def main():
	number = int(input('your number: '))
	print(f'the sum of number is {summ(number)}: ')
	
def summ(num):
	if num == 0:
		return 0
	else:
		return num + summ(num - 1)
	
main()