def main():
	Number = int(input('your numbers '))
	isEven = sum_all_even(Number)
	print(isEven)
	
def sum_all_even(num):
	if num == 0:
		return 0
	else:
		if (num % 10) % 2 == 0:
			
			return (num % 10) + sum_all_even(num // 10)
		else:
			return sum_all_even(num // 10)
	
	
main()