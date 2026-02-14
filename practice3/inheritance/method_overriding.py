class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    pass


#2
class Animal:
    def speak(self):
        print("Animal makes a sound")

class Dog(Animal):
    def speak(self):   # overriding
        print("Dog barks")

#3
class Animal:
    def speak(self):
        print("Animal sound")

class Dog(Animal):
    def speak(self):
        print("Bark")

class Cat(Animal):
    def speak(self):
        print("Meow")
