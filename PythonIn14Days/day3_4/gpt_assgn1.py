def main():

    digit = int(input('digits: '))
    print(f'sum of digits is {Ndigits(digit)}')

def Ndigits(num):
    if num == 0:
        return 
    else:
        Ndigits(num - 1)
        print(num)




main()