def main():
	N = int(input('your number: '))
	print(f'the rcursn of {N} is: ')
	prtn(N)
	
def prtn(num):
	if num == 0:
		return 0
	else:
		print(num)
		prtn(num - 1)
	
main()