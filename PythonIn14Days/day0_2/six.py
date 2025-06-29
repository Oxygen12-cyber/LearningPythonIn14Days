phrase = input('what food do you like: ')

a = phrase.find("beans")
if a != False or 0 :
    print('beans is in the sentence')
else:
    print('beans is not in the sentence')


phrase = input('what food do you like: ')
if "beans" in phrase:
    print('beans is in the sentence')
else:
    print('beans is not in the sentence')

