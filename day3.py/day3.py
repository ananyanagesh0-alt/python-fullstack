
# ########## global scope #################
# name = "Rani"
# def student():
#     print(name)
# student()
# print(name)


# ############### local scope #################
# def student():
#     age = 20
#     print(age)
# student()




######################## both global n local scope #####################
# name = "Rani"
# def student():
#     age = 20
#     print(name)
#     print(age)
# student()




# name = "usha"
# name = "Rani"
# def display():
#     name = "Thanvitha"
#     name = "Ananya"
#     print(name)
# display()
# print(name)


###################### without lambda #####################

# def square(num):
#     return num*num  

# num = square(5)
# print(num)

# ########################## lambda ##########################
# square = lambda num:num*num
# print(square(5))


# cube = lambda num:num*num*num
# print(cube(2))

# add = lambda a,b:a+b
# print(add(5,6))

# subtract = lambda a,b:a-b
# print(subtract(5,6))    

# divide = lambda a,b:a/b
# print(divide(5,6))

# largest = lambda a,b:a if a>b else b
# print(largest(5,6))

# multiplication = lambda a,b:a*b
# print(multiplication(4,3))


# def countdown(n):
#     if n==0:
#         return
#     print(n)

#     countdown(n-1)
# countdown(5)


# def factorial(n):
#     if n==0:
#         return 1
#     else:
#         return n*factorial(n-1)
# print(factorial(5))

# def power(a,b):
#     if b==0:
#         return 1
#     return a*power(a,b-1)
# print(power(2,3))



# def prime(n,i=2):
#     if n<=2:
#         return True if n==2 else False
#     if n%i==0:
#         return False
#     if i*i>n:
#         return True
#     return prime(n,i+1)
# print(prime(11))
