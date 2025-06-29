name = str(input('your name: '))

age = int(input('your age: '))
num = str(len(name))
print('Hello, ' + name.upper() + '. You are ' + str(age) + ' years old.')
print(f'Hello {name.upper()} you are {age} years old.')
print('thank you: your name has' + " " + num + ' letters in it')
print(f'thank you: your name has {num} letters in it')

