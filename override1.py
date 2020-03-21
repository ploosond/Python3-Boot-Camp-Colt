class Animal():
    def speak(self):
        rasie NotImplementedError("Subclass needs to implement this method")

class Dog(Animal):
    def speak(self):
        return "woof"

class Cat(Animal):
    def speak(self):
        return "meow"

class Fish(Animal):
    pass

d = DOg()
print(d.speak())
f = Fish()

print(f.speak())