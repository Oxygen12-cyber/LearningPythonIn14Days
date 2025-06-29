def main():

    word_case = input('your word: ')
    print(f'the camelcase cnversion to snake case of your word is {detect_cap(word_case)}')



def detect_cap(word):
    global exact
    for i in word:
        if i.isupper():
            exact = word.index(i)
    str1 = word[:exact]
    str2 = word[exact:]
    concat_string = str1 + '_' + str2
    return concat_string


if __name__ == "__main__":
    main()