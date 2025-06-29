def main():
	Word = input('your word: ')
	isTrue = is_all_lower(Word)
	print(isTrue)
		
def is_all_lower(word):
	if len(word) == 0:
		return True
	else:
		if word[0].islower() == True:
			return is_all_lower(word[1:])
		else:
			return False
			

main()