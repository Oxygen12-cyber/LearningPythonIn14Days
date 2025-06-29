def main():
    factor = int(input('your number'))
    print(f'The factorial of your number is: {factorial(factor)}')
        
def factorial(num):
    if num == 0:
        return 1
    elif num == 1:
        return 1
    else:
        return num * factorial(num - 1)
    
main()