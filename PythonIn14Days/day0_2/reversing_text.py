text = str(input('your word: '))
reversed = text[::-1]
not_reversible = "not reversible" if len(text) > 10 else "reversible"
print(not_reversible)
print(reversed)
