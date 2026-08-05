# SheryiansSchool = "students"  #pascal case
# sheriansSchool = "students" #camel case
# sherians_school= "students" #snake case


# # DATA TYPES
# a = 34
# b = 23.4
# c = 23/5
# v = 34j
# print(type(v))


# # strings
# st = 'sfdshhds!@#$%&&**1235677'
# print(type(st))
 


# y=True
# z=False
# print(type(y))
# print(type(z))

# z="z"
# print(ord(z))

# a=65
# print(chr(a))

# # INDEXING
# a="SHER"
# print(a[-2],a[3])

# # string slicing
# a = "SHER CODER"
# print(a[0:4:1])

# print(a[5::1])
 
# # print(a[::3])

# #  TYPE CONVERSIONS


# a = 12
# a = str(a)
# print(type(a))

# # Boolean values
# a = []
# print(bool(a))



# # implict expression
# a= 12
# print(12/3)


# name = "UMAR"
# age = "21"
# print(name,age)

# raw string
# print("hello my name is",name,"and my age is",age)


#formatted string
# print(f"my name is {name} and my age is {age}")


# age = int(input("hello what is u r age: "))

# print(age)
# print(type(age))


# EXAMPLE 

# number = int(input("enter your number: "))
# print("The number is:", number)

# age = int(input("enter your age: "))
# print("age is:", age)



#  OPERATORS
# ARITHMETIC 
# a = 5
# b = 20
# print("after adding:",(a + b))
# print(b - a)
# print(b * a)
# print(b / a)
# print(b // a)
# print(b ** a)
# print(8 ** 2) # square, cube 
# print(5 ** 100)

# print(32 % 5)


#assignment operator

# a=23
# print(a)

# COMPUND ASSIGNMENT OPERATIONS

# a = 20
# a += 40
# a += 30


# a -=10
# print(a)

# SIMPLE COMPARISISON OPERATOR 

# a = 12.5
# b = 12
# print(a == b)

# print(a != b)
# print(a>b)
# print(a >= b)

# print(45<=27)



# print(ord("A"))
# print(ord("B"))
# print(ord("C"))

# print("A" > "B")

# print(ord("M"))
# print(ord("z"))

# print("MD" < "UMAR")

# LOGICAL OPERATORS

# print(10 < 12 and 10>9 and 42 == 42 and 9 < 3)


# print(10 < 12 or 10>9 or 42 == 42 or 9 < 3)


# print(not 12 == 12)

# IF ELSE

# a = 13

# if a < 10:
#     print("yes it is correct")
# else:
#     print("NO it is  wrong") 

# # TRUE
# b = 11

# if b > 10:
#     print("yes it is correct")
# else:
#     print("NO it is  wrong") 



# #EXAMPLE

# money = int(input("PLEASE ENTER THE AMOUNT:-"))

# if money == 10:
#     print(" I WILL BUY A CHOCO BAR ICE CREAM")

# elif money <= 20:
#     print("I WILL BUY A MANGO DOLLY")

# elif money == 30:
#     print("I WILL BUY A VANILLA ICE CREAM")

# elif money == 40:
#     print("I WILL BUY A CHOCOLATE")

# else:
#     print("I WILL BUY A CONE ICE CREAM")

# QUESTIONS ON CONDITIONAL Q1

# num1 = int(input("ENTER THE FIRST NUMBER:- "))
# num2 = int(input("ENTER THE SECOND NUMBER:- "))

# if num1 > num2 :
#     print(" NUMBER 1 IS GREATER")
# elif num2 > num1:
#     print("NUMBER 2 IS GREATER")
# else:
#      print(" BOTH THE NAMES ARE SAME")


# Q2

# gender = input("ENTER YOUR GENDER AS CHARACTER(M OR F):")
# if gender == 'M' or gender == 'm' :
#     print("GOOD MORNING SIR")

# elif gender == 'F' or gender == 'f':  
#     print("GOOD MORNING MAM")
# else:
#     print("UNIDENTIFIED GENDER")

# Q3
# num =int(input("ENTER THE NUMBER:-"))

# if num%2 == 0:
#     print("THE NUMBER IS EVEN")
# else:
#     print("THE NUMBER IS ODD")

# Q4 REFER FORMATTED STRING CAREFULLY 



# name = input("ENTER YOUR NAME:-")
# age = int(input("ENTER YOUR AGE:-"))

# if age >= 18:
#     print(f"HELLO {name} YOU R A VALID VOTER")
# else:
#     print(f"HELLO {name} YOU R NOT A VALID VOTER")

# Q5 LEAP YEAR (REFER ONE MORE TIME)

# year =int(input("ENTER THE YEAR:-"))
# if year % 100== 0  and year % 400 == 0:
#     print("THIS IS LEAP YEAR")
# elif year % 400 != 0 and year %4 ==0:
#     print("IT'S A LEAP YEAR")

# else:
#     print("NOT A LEAP YEAR")


# Q6 IF-ELSE LADDER 
# temp = int(input("ENTER YOUR TEMPRATURE:-"))

# if temp<0:
#     print("FREEZING COLD")
# elif temp >=0 and temp<10:
#     print("VERY COLD")

# elif temp>=10 and temp<30:
#     print("PLESANT")

# else:
#     print("TEMPERATURE IS VERY HOT")



# LOOPS

# FOR LOOP
# RANGE  correct way


# LETS PRINT A TABLE
# for i in range(5,51,5):
#     print(i)


# n = int(input("ENTER THE TABLE U WANT:-"))
# for i in range(n,n*10+1,n):
#     print(i)



# # OR 

# a = range(1,21,2)

# for i in a :
#     print(i)

# for i in range(50,19,-1):
#     print(i)


# a = "MOHAMMED UMAR"
# for i in range(0,13,1):
#     print(a[i])


# USING OF INDEX ON STRINGS

# a = "I AM LEARNING PYTHON FROM SHERIYANS CODING SCHOOL IN YOUTUBE"
# for i in range(len(a)):
#     print(a[i])

# DIRECTLY ON STRINGS
# a = "MOHAMMED UMAR"
# for i in a:
#     print(i)



# # break statement
# for i in range(1,15):
#     if i == 6:
#         break
#     else:
#         print(i)



# # CONTINUE STATEMENT

# for i  in range(2,30):
#     if i == 15:
#         continue
#     print(i)

# for i in range(1,21):
#     if i == 56:5
#         print("break statement is executed")
#         break
#     print(i)
# else:
#     print("break statement not executed")



# QUESTIONS ON FOR LOOP

# n = int(input("enter the number of time u want to print:-"))
# for i in range(n):
#     print("HELLO WORLD")

#   Q2 
# n = int(input("ENTER THE NATURAL NUMBER UP TO U WANT:-"))
# for i in range(1,n+1):
#     print(i)

# Q3 

# n = int(input("ENTER THE NUMBER:-"))
# for i in range(n,0,-1):
#     print(i)

# Q4

# n = int(input("ENTER THE TABLE U WANT:-"))
# for i in range(1,11):
#     print(f"{n} * {i} = {n*i}") 

# Q5


# n = int(input("ENTER THE NUMBER U WANT TO PRINT:-  "))
# sum = 0
# for i  in range (1,n+1):
#     sum = sum + i
# print(f"the sum is {sum}")

# n = int(input("ENTER THE NUMBER U WANT TO PRINT:-  "))
# fact = 1
# for i  in range (1,n+1):
#     fact = fact * i
# print(f"the factorial is {fact}")


# n = int(input("ENTER THE NUMBER:- "))
# even = 0
# odd = 0
# for i in range(1,n+1):
#     if i%2 ==0:
#         even = even + i
#     else:
#         odd = odd + i
# print(f"your even and odd sum are {even} , {odd}")


# n = int(input("ENTER THE NUMBER:- "))
# for i in range(1,n+1):
#     if n%i == 0:
#         print(i)


# n = int(input("CHECK THE NUMBER IS PERFECT OR NOT:- "))
# sum = 0
# for i in range(1,n):
#     if n%i == 0:
#         sum = sum + i 
# if sum == n:
#     print("the number is perfect number")
# else:
#     print("the number is not a perfect number")


# n = int(input("CHECK THE NUMBER IS PRIME OR NOT:- "))
# count = 0
# for i in range(1,n+1):
#     if n%i == 0:
#         count = count + 1
# if count == 2:
#     print("your number is prime")
# else:
#     print("your number is not prime"   )



# REVERSE A STRING 


# a = "Mohammed Umar"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# print(b)



# PALINDROME

# a = "M"
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("its a palindrome string")
# else:
#     print("not a palindrome string")

#  OR 

# a = input("ENTER THE STRING:- ")
# b = ""
# for i in range(len(a)-1,-1,-1):
#     b = b + a[i]
# if b == a:
#     print("its a palindrome string")
# else:
#     print("not a palindrome string")

## COUNT ALL THE STRINGS,NUMBERS & CHARACTERS IN THE STRINGS

# n = input("enter the string: ")
# dig = 0
# char = 0
# spchr = 0

# for i in n:
#     if i.isdigit():
#         dig +=1
#     elif i.isalpha():
#         char +=1
#     else:
#         spchr +=1
# print(f" THE DIGITS ARE {dig}\n THE CHARACTERS ARE {char}\n THE SPECIAL CHARCATERS ARE {spchr}")


# print(dir(str))


# WHILE LOOOOOP

# a = 1
# b = ""
# while a <= 30:
#     print(a)
#     a = a + 1


# a = int(input("enter the number :- "))
# while a > 0:
#     print(a % 10)
#     a =a // 10

# reverse of a number

# a = int(input("enter the number :- "))
# rev =0
# while a > 0:
#     rev = rev *10 + a % 10
#     a =a // 10
# print(rev)


# while loop palindrome

# a = int(input("enter the number :- "))
# copy = a
# rev =0
# while a > 0:
#     rev = rev *10 + a % 10
#     a =a // 10

# if copy == rev:
#     print("pallindromic number")
# else:
#     print("not a palindromic number")


# RANDOM NUMBER GUESSING GAME

# import random
# num = random.randint(1,200)
# tries = 0

# while True:
#     guess = int(input("GUESS THE NUMBER:-"))
#     if num == guess:
#         tries += 1
#         print(f" U GUESSED THE RIGHT NUMBER {tries} tries")
#         break
#     elif num < guess:
#         tries += 1
#         print(" LITTLE LOWER")
#     elif num > guess:
#         tries += 1
#         print("LITTLE HIGHER") 
#     else:
#         tries +=1
#         print("sorry u guessed the wrong number")    

# FUNCTIONS 

# def hello():
#     print("HI HOW R U?")
# hello()

# PARAMETERS AND ARGUMENTS

# def sum(a,b):
#     print("the sum of the numbers are", a+b)
# sum(10,2)


# KEYWORD ARGUMENT
# def hello(name,age):
#     print(f"your name is {name} annd u r age is {age}")
# hello(age = 21,name= "UMAR")


# default argument
# def sum(a,b=45):
#     print(f"sum of numbers : {a+b}") 
# sum(10,12)
 

# EXAMPLE ON PARAMETERS AND ARGUMENTS

# def pallindrome(st):
#     b=""
#     for i in range(len(st)-1,-1,-1):
#         b = b + st[i]
#     if b == st:
#         return(f"{st} is a pallindromic string ")
#     else:
#         print(f"{st} is not  a pallindromic string")

# print(pallindrome("NAMAN"))
# pallindrome("UMAR")

 # RETURN USE-CASE

# def hello():
#     return "HELLO THIS IS THE RETURN STATEMENT"
# print(hello())


# def num():
#     return 10
# print(num())  


# def sum(a,b):
#     return(a+b)
# print(sum(10,2))
# print(sum(12,5))

# DATA STRUCTURE INBUILT
# LISTS 

# a = [12,13,15,16,17,18,True,"banana"]
# a[1]=12333
# print(a[2])
# print(a[0:5:2])
# print(a[-2])
# print(a[1])



# LIST TRAVERSING & METHODS 
# 1 WAY USING INDEX

# a = [12,13,14,15,1,16,]
# for i in range(len(a)):
#     print(a[i])

# 2nd WAY directly on values

a = [12,13,14,15,1,16,]
for i in a:
    print(i)
