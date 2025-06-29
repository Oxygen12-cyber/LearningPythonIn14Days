password = input(str('Enter your Password: '))
one_of_pass = password[0]
if one_of_pass == None:
    print('reenter your password')
else:
    print(one_of_pass)