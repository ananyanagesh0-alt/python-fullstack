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
class father:
    def car(self):
        print("Father has a car")

class mother:
    def house(self):
        print("Mother has a house")

class son(father, mother):
    def bike(self):
        print("Son has a bike")

s = son()
s.car()
s.house()
s.bike()

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


