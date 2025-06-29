def main():
    class Car:
        def __init__(self, brand, year):
            self.brand = brand
            self.year = year

    car1 = Car('Toyota', 2006)

    car_brand = car1.brand
    car_year = car1.year

    print(f'the car is a {car_brand} from year {car_year}')



if __name__ == '__main__':
    main()