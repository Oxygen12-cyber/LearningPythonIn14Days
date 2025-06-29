def main():
	charc = input('your character: ')
	word = input('your Word: ')
	counts = count_char(charc, word)
	print(f'the word {word} appears {counts} times in {charc} ')
	
def count_char(char, wrd):
	if len(char) == 0:
		return 0
	else:
		if char[0] == wrd:
			return 1 + count_char(char[1:], wrd)
		else:
			return count_char(char[1:], wrd)
	
main()