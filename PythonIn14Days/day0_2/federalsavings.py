def main():
    while True:
        greeting = input('Greeting: ')
        if (greeting == 'hello') or (greeting == 'Hello'):
            print('$0')

        elif (greeting[0] == 'h')or  (greeting[0] == 'H'):
            print('$20')

        else:
            print('$100')
            break

main()