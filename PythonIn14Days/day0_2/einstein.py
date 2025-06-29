c = int(300000000)
def einstein(mass):
    E = mass * (c ** 2)
    return E

def main():
    Mass = int(input('the mass of the object: '))
    print(f'The energy is {einstein(Mass)} joules')

main()