class Person():

    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        
    def fullname(self):
        concat = self.first_name + ' ' + self.last_name
        return concat
        
person = Person('Yukihiro', 'Matsumoto', 47)
print(person.fullname())
print(person.age)
