string1 = 'Becomes'
string2 = 'becomes'
string3 = 'BEAR'
string4 = '   beautiful'

string1 = string1.lower()
string2 = string2.lower()
string3 = string3.lower()
string4 = string4.lower().strip()

print(string1.startswith('be'))
print(string2.startswith('be'))
print(string3.startswith('be'))
print(string4.startswith('be'))
