class Human:
    def __init__(self, first, last, age):
        self.first = first
        self.last = last
        if age >= 0:
            self._age = age
        else:    
            self._age = 0

    # def get_age(self):
    #     return self._age

    # def set_age(self, new_age):
    #     if new_age >= 0:
    #         self._age = new_age
    #     else:    
    #         self._age = 0

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, value):
        if value >= 0:
            self._age = value
        else:
            raise ValueError("age can't be negative")



    @property
    def full_name(self):
        return f'{self.first} {self.last}'

    @full_name.setter
    def full_name(self, name):
        self.first, self.last = name.split (" ")

jane = Human("Jane", "Goodall", 34)
# print(jane.get_age())
# jane.set_age(10)
# print(jane.get_age())
print(jane.age)
jane.age = 50
print(jane.age)
print(jane.full_name)
jane.full_name = "Tim Minchin"
print(jane. __dict__)
