old_smiley =':)'
old_sady = ':('
new_smiley = '😊'
new_sady = '😞'
Word = str(input('your word wih an emoji: '))
def convert(word):
    word = word.replace(old_smiley, new_smiley)
    word = word.replace(old_sady, new_sady)
    return word

    

def main():
    print(f'{convert(Word)}  \nyour word has been converted to new emoticon format ')
    

main()
