while True:	
	number = int(input('the number: '))
	number2 = int(input('divisor: '))
	if number2 < 1:
		break
	else:
		division = number // number2
		remainder = number % number2
		print(f'{number} // {number2} = {division} remainder {remainder}')
