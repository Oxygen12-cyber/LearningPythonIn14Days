def main():
    class Dog():
        def __init__(self, name, type):
            self.name = name
            self.type = type

    dog1 = Dog()
    dog2 = Dog()
    dog1.name = 'Fredric'
    dog2.name = 'jamie'
    dog1.type = 'labrador'
    dog2.type = 'collie'

    print(f'my moms dog is {dog1.name} and my dog is {dog2.name} \n mine is a {dog2.type} and my mom is a{dog1.type}')

if __name__ == "__main__":
    main()