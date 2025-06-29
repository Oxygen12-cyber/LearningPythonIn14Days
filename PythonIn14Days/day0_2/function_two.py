def area(length, width):
   return str(length*width)
    

def main():
    former_house = area(12, 11)
    new_house = area(30, 22)
    print(f'{former_house} is smaller than {new_house}')


main()