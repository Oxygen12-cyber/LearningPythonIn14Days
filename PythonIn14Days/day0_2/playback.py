def play_back(word):
    replacing = word.replace(" ", "----")
    return replacing

def main():
    Word = str(input("your word: "))
    print(play_back(Word))

main()