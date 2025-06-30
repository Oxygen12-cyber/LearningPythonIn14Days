#add display_info method to display the model's info
def main():
    class Car:
        def __init__(self, model, year):
            self.model = model
            self.year = year

        def display_info(self):
            print(f'This car is a {self.model} from the year {self.year}')

    car = Car('Toyota', 2006)
    Car.display_info(car)

if __name__ == '__main__':
    main()