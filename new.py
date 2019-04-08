# print("hello")
# print("this is \\\\ double backslash")
# print("these are /\\/\\/\\/\\/\\ mountains")
# print("he is \t awesome")
# print("\\\" \\n \\t \\\'")
# print(r"\' \" \n \t")
# number1, number2, number3 = input("enter your no.1 no.2 no.3 ").split()
# print(f"number1 {number1} number2 {number2} number3 {number3}")
# print("number1")
# print("number2")
# print("number3")
# sum =int(number1) + int(number2) + int(number3)
# print(int(sum))
# # average = int(number1)  + int(number2) + int(number3) / 3
# number1, number2, number3 = input("Enter no sep by comma : ").split(",")
# print(f"average is = {(int(number1) + int(number2) + int(number3)) / 3}")
# name = input("Enter your name : ")
# print(f"your ans is : {name[::-1]}")
# name, char = input("Enter your name and single character : ").split(",")
# print(f"your name length is = {len(name)}")
# # name1 = name.lower()
# # print(f"your char repeat in {name1.count(char)}")
#  print(f"your ans is {name.lower().count(char.lower())}")
# print('this is \\\\ backslash')
# print("this are mountains /\\/\\/\\/\\")
# print("he is \t awesome")
# print("\\\' \\\" \\n \\t")
# name = input("Enter your name : ")
# print(name[::-1])
# name , latter = input("Enter your name and latter sep by comma : ").split(",")
# print(f"length of your name is {len(name)}")
# print(f"latter count is {name.lower().count(latter.lower())}")
# print(f"latter count is {name.strip().lower().count(latter.strip().lower())}")
# string = ("she is beautiful and she is good dancer")
# print(string.replace("is","was",1))
# print(len(string))
# name = input("Enter your name : ")
# print(f"your name lenght is {len(name)}")
# print(name.center(len(name)+ 8, "*"))
# winning_number = 34
# guess_number = input("enter your no : ")
# guess_number = int(guess_number)
# if guess_number == winning_number:
#     print("you win !!!!")
# elif guess_number < winning_number:
#     print("too low")
# elif guess_number > winning_number:
#     print("too high")
## name = input("Enter your name : ")
# age = input("Enter your age : ")
# age = int(age)
# if (name[0] == 'a' or name[0] == 'A') and age > 10:
#     print("you can watch coco movie")
# else:
#     print("sorry you cannot watch coco movie")
## n = input("Enter your number : ")
# n = int(n)
# total = 0
# i = 1
# while i<=n:
#     total += i
#     i += 1
# print(f"your answer is {total}")

# number = input("Enter your no. more than one digit : ")
# total = 0
# i = 0
# while i < len(number):
#     total += int(number[i])
#     i += 1
# print(total)

# name=input("Enter your name : ")
# temp_var = ""
# i=0
# while i< len(name):
#     if name[i] is not temp_var:
#         print(f"{name[i]} : {name.count(name[i])}")
#         i+=1    

# number = input("enter your number : ")
# total=0
# i=0
# for i in range(0,len(number)):
#     total+=int(number[i])
#     i+=1
# print(total)

# import random
# number=int(input("Guess the number between 1 to 100 : "))
# winning_number=random.randint(1,100)
# number=int(number)
# guess=1
# game_over=False
# i=1
# while not game_over:
#     if number == winning_number:
#         print(f"you win and you guess this number in {guess} time")
#         game_over=True
#     else:
#         if number > winning_number:            
#             print("too high")
#             guess += 1
#             number = int(input("Guess again : "))
#         else :
#             print("too low")
#             guess += 1
#             number = int(input("Guess again : "))

# #DRY
# import random
# number=int(input("Guess the number between 1 to 100 : "))
# winning_number=random.randint(1,100)
# number=int(number)
# guess=1
# game_over=False
# i=1
# while not game_over:
#     if number == winning_number:
#         print(f"you win and you guess this number in {guess} time")
#         game_over=True
#     else:
#         if number > winning_number:            
#             print("too high")
           
#         else :
#             print("too low")

#         guess += 1
#         number = int(input("Guess again : "))

## def last_latter(latter):
#     return name[-1] 

# name=input("Enter your name or number : ")
# print(last_latter(name))

# #def odd_eve(odd_eve):
#     if (number%2) == 0:
#             return("number is even")
#     else:
#             return("number is odd")
   
# number=int(input("Enter your number : "))
# print(odd_eve(number))

# def odd_eve(odd_eve):
#     if (number%2) == 0:
#         return("number is even")
#     return("number is odd")
        
# number=int(input("Enter your number : "))
# print(odd_eve(number))

# def is_even(num):
#     return num%2==0
# number=int(input("Enter your number : "))
# print(is_even(number))

##def greter(a,b):
#     if a>b:
#         return(f"{a} is greter")
#     else:
#         return(f"{b} is greter")

# num1= int(input("Enter your 1st number : "))
# num2= int(input("enter your 2nd number : "))
# print(greter(num1,num2))

# def greter(a,b,c):
#     if a>b and a>c:
#         return(f"{a} is greter")
#     elif b>a and b>c:
#         return(f"{b} is greter")
#     else:
#         return(f"{c} is greter")

# num1= int(input("Enter your 1st number : "))
# num2= int(input("enter your 2nd number : "))
# num3= int(input("Enter your 3rd number : "))
# print(greter(num1,num2,num3))
    
## def is_palindrom(strn):
#     revers = strn[::-1]
#     if strn == revers:
#         return ("string is palindrom")
#     else:
#         return ("string is not palindrom")

# strn=input("enter your string : ")
# print(is_palindrom(strn))

## def is_palindrom(word):
#     return word == word[::-1]
# print(is_palindrom("naman"))

## number =list(range(1,11))
# def sqr(l):
#     sqr = []
#     for i in l:
#         sqr.append(i**2)
#     return sqr
# print(sqr(number))

## number=list(range(1,11))
# def rev(l):
#     rev=[]
#     for i in range(len(l)):
#         pop1=l.pop()
#         rev.append(pop1)
#     return rev
# print(rev(number))

## def revs(l):
#     rev=[]
#     for i in l:
#         rev.append(i[::-1])
#     return rev 
# number=['asd','fgh','jkl']   
# print(revs(number))

# def filter(l):
#     odd_nums=[]
#     even_nums=[]
#     for i in l:
#         if i%2 == 0:
#             even_nums.append(i)
#         else:
#             odd_nums.append(i)
#     output=[odd_nums,even_nums]
#     return output
# nums=[1,2,3,4,5,6,7]
# print(filter(nums))

# def common_num(l1,l2):
#     output=[]
#     for i in l1:
#         if i in l2:
#             output.append(i)
#     return output
# print(common_num([1,2,5,8], [1,2,7,6]))

# def count_num(l):
#     count=0
#     for i in l:
#         if type(i) == list:
#             count +=1
#     return count
# number=[1,2,3,[1,2],[3,4]]
# print(count_num(number))

# def cube(n):
#     cub={}
#     for i in range (1,n+1):
#         cub[i] = i**3
#     return cub
# print(cube(10))

## user={}
# name=input("Enter your name : ")
# age=input("Enter your age : ")
# fav_movie=input("Enter your favourite movie : ").split(',')
# fav_song=input("Enter your favourite song : ").split(',')

# user['name']= name
# user['age']=age
# user['fav_movie']=fav_movie
# user['fav_song']=fav_song
# # print(user, end='\n')
# for key, value in user.items():
#     print(f"{key} : {value}")

# def rev(l): 
#     return [name[::-1]for name in l]
# print(rev(['asd','fgh','jkl']))

# l=[1,1.0,3,[1,2,3],True,False]
# def filter(l):
#     return [str (i) for i in l if (type(i)==int or type(i)==float)]
# print(filter(l))

## def cubes(num,*args):
#     if args:
#         return[i**num for i in args]
#     else:
#         return"you didn't pass"
# nums=[1,2,3]
# print(cubes(2,*nums))

## def rev(l,**kwargs):
#     if kwargs.get('reverse_str') == True:
#         return[name[::-1].title() for name in l]
#     else:
#         return [name.title() for name in l]
# names=['abhay','vampax']
# print(rev(names,reverse_str = True))
 
## def find_pos(l,target):
#     for pos,name in enumerate(l):
#         if name == target:
#             return pos
#     return -1
# names=['ab','avdsf','Abhay']
# print(find_pos(names,'Abhay'))

## from functools import wraps
# import time
# def calculate_time(f):
#     @wraps(f)
#     def wrapper(*args,**kwargs):
#         print(f"Executing ....{f.__name__}")
#         t1=time.time()
#         return_value = f(*args,**kwargs)
#         t2=time.time()
#         total_time=t2-t1
#         print(f"This function took {total_time} time")
#         return return_value
#     return wrapper
# @calculate_time
# def square_finder(n):
#     return[i**2 for i in range(1,n+1)]
# square_finder(1000)

## def even_num(n):
#     for i in range(1,n+1):
#         # for i in range(2,n+1,2):
#         if n%2==0:
#             yield i
# for n in even_num(20):
#     print(n)

## class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name=brand_name
#         self.model_name=model_name
#         self.price=price
# l1=Laptop('hp','omen',150000)
# print(l1.brand_name)

# class Laptop:
#     def __init__(self,brand_name,model_name,price):
#         self.brand_name=brand_name
#         self.model_name=model_name
#         self.price=price
#     def discount(self,n):
#         self.price
#         off_price=(n/100)*self.price
#         return self.price - off_price
# l1=Laptop('hp','omen',150000)
# print(l1.discount(30))
 
# class Person:
#     count_instance=0
#     def __init__ (self,f_name,l_name,age):
#         Person.count_instance+=1
#         self.fname=f_name
#         self.lname=l_name
#         self.age=age
# p1=Person ('Abhay','Kanoji',22)
# print(Person.count_instance)

# def division(a,b):
#     try:
#         return a/b
#     except ZeroDivisionError as err:
#         # print("you cannot enter 0 no.")
#         print(err)
#     except TypeError as err:
#         print('numbers must be int or float')
#     except:
#         print("Unexpected error")
# print(division(10,5))

# echo -e "data" >>> n1.txt for creating file

# with open("n1.txt",'w') as f:
#     f.write('Harshit,100\nMohit,50\nAAditya,200\nNitish,500')

# with open("n1.txt",'r') as rf:
#     with open("n2.txt",'a') as wf:
#         for line in rf.readlines():
#             name,n1=line.split(',')
#             wf.write(f"{name}\'s salary is {n1}")



    