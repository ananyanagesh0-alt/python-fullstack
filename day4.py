# class student:
#     def __init__(self,name,age):
#         self.name = name
#         self.age = age

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)      

# s1=student("Rani",20)
# s1.display()

# class employee:
#     def __init__(self,name,age,salary,department):
#         self.name=name
#         self.age=age
#         self.salary=salary
#         self.department=department

#     def display(self):
#         print("Name:",self.name)
#         print("Age:",self.age)
#         print("Salary:",self.salary)
#         print("Department:",self.department)


# e1 = employee("John",30,50000,"IT")
# e2 = employee("Alice",28,60000,"HR")
# e1.display()
# print()
# e2.display()

############# single inheritance ####################
# class Animal:
#     def eat(self):
#         print("Animal is Eating")


# class Dog(Animal):
#     def bark(self):
#         print("Dog is Barking")

# d = Dog()
# d.eat()
# d.bark()

############### Multi-level ###############
# class grandfather:
#     def house(self):
#         print("Grandfather has a house")
# class father(grandfather):
#     def car(self):
#         print("father has a car")
# class son(father):
#     def bike(self):
#         print("Son has a bike")
# s= son()
# s.house()
# s.car()
# s.bike()



############### Multiple inheritance #####################
# class father:
#     def car(self):
#         print("Father has a car")

# class mother:
#     def house(self):
#         print("Mother has a house")

# class son(father, mother):
#     def bike(self):
#         print("Son has a bike")

# s = son()
# s.car()
# s.house()
# s.bike()

################ hierarchical inheritance #####################
# class father:
#     def father_property(self):
#         print("Father has a property")

# class son(father):
#     def mother_property(self):
#         print("mother has a property")

# class daugther(father):
#     def son_property(self):
#         print("son has a property")

# s=son()
# s.father_property()
# s.mother_property()

###################### polymorphism ###############
# class car:
#     def move(self):
#         print("Car is moving")
# class boat:
#     def move(self):
#         print("Boat is sailing")
# class aeroplane:
#     def move(self):
#         print("Aeroplane is flying")
# vehicles = [car(), boat(), aeroplane()]
# for vehicle in vehicles:
#     vehicle.move()

#################### abstract class #####################
# from abc import ABC, abstractmethod

# class Vehicle(ABC):
#     @abstractmethod
#     def start(self):
#         pass

# class Car(Vehicle):
#     def start(self):
#         print("Car is starting")

# class Bike(Vehicle):
#     def start(self):
#         print("Bike is starting")
# car = Car()
# car.start() 
# bike = Bike()
# bike.start()


from abc import ABC, abstractmethod
class Animal:
    @abstractmethod
    def sound(self):
        pass
class Dog():
    def sound(self):
        print("Dog barks")  
class Cat():
    def sound(self):
        print("Cat meows")
class Cow():
    def sound(self):
        print("Cow moos")
class Lion():
    def sound(self):
        print("Lion roars")
dog = Dog()
dog.sound() 
cat =Cat()
cat.sound() 
cow = Cow()
cow.sound() 
lion = Lion()
lion.sound()

#################### encapsulation #####################
class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks
    def get_marks(self):
        return self.marks
    def set_marks(self, marks):
        if marks >= 0 and marks <= 100:
            self.marks = marks
        else:
            print("Invalid marks. Please enter a value between 0 and 100.")
    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks) 
student1 = Student("Rani", 20)
student1.set_marks(85)
student1.display()

################## miniproject #################
from abc import ABC, abstractmethod

class Employee(ABC):
    def __init__(self,name,salary):
        self.name = name
        ## Encapsulation
        self.__salary = salary
    def get_salary(self):
        return self.__salary
    @abstractmethod
    def calculate_salary(self):
        pass
    def display(self):
        print("Name:",self.name)
        print("Salary:",self.calculate_salary())
#inheritance
class Developer(Employee):
    def calculate_salary(self):
        #developer gets 10% bonus
        bonus = self.get_salary() * 0.1
        return self.get_salary() + bonus
class Manager(Employee):
    def calculate_salary(self):
        #manager gets 20% bonus
        bonus = self.get_salary() * 0.2
        return self.get_salary() + bonus
#objects
developer = Developer("Rani", 50000)
manager = Manager("Ananya", 60000)
#Polymorphism
developer.display()
print()
manager.display()

