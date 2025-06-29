def main():
    word = input('what is the answert to the great question of life, the universe, and everything?: ')
    FT1 = 'forty-two'
    FT2 = 'Fortytwo'
    FT3 = 'FORTY-TWO'
    FT4 = 'forty two'
    FT5 = '42'

    if FT1 in word or FT2 in word or FT3 in word or FT4 in word or FT5 in word:
        print('Yes')
    #elif FT2 in word:
    #    print('yes')
    #elif FT3 in word:
    #    print('yes')
    #elif FT4 in word:
    #    print('yes')
    #elif FT5 in word:
    #    print('yes')
    #else:
    #    print('NO')
    ...

main()