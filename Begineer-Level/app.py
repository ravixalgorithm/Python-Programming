"""Start:"""
# print("Hello world");


"""Drawing a Shape"""
# print("    /|")
# print("   / |")
# print("  /  |")
# print(" /   |")
# print("/____|")


"""Variables and DATA TYPES"""
character_name = "Ravi";
character_age = 20;
# print("My name is",character_name,"and I am",character_age,"years old.")


"""Working with Strings"""
phrase = "Giraffe Academy" #str
# print("original:",phrase)

'''to lower case => str.lower()'''
# print(phrase.lower())

'''to upper case => str.upper()'''
# print(phrase.upper())

'''check upper and lower case => str.isupper() , str.islower()'''
# print(phrase.isupper())
# print(phrase.islower())
# print(phrase.upper().isupper())

'''length of string => len(str)'''
# print(len(phrase))

'''print character from str => str[index]'''
# print(phrase[0])

'''index of character/word => str.index("ch/word")'''
# print(phrase.index("G"))
# print(phrase.index("ffe"))

'''replacing a string => str.replace("word to replace","with whom")'''
# print(phrase.replace("Giraffe","Elephant"))


"""Working with Numbers"""

'''Converting a number to string => str(number)'''
my_num = 5;
# print(str(my_num))

'''Absolute value[-5 == 5] of the number => abs(number)'''
my_num = -5
# print(abs(my_num))

'''power of a number => pow(number, power)'''
# print(pow(3,2))

'''max or min of two numbers => max(num1, num2) , min(num1,num2)'''
# print(max(5,3))
# print(min(3,6))

'''round off the number => round(number)'''
# print(round(3.245))

'''after importing math lib.'''
from math import *
'''floor of a number => floor(number)'''
# print(floor(4.5))
'''ceiling of a number => ceil(number)'''
# print(ceil(4.5))
'''sq root of any number => sqrt(number)'''
# print(sqrt(36))


"""Getting input from the user"""
# name = input("Enter the name: ")
# age = input("Enter the Age: ")
# print("Hello",name,", you are",age,"years old")


"""Basic Calculator"""
# num1 = input("Enter number 1: ")
# num2 = input("Enter number 2: ")
# sum = float(num1) + float(num2)
# print(sum)


"""Mad Libs Game"""
# nounSingular = input("Enter a Singular Noun: ")
# nounPlural = input("Enter the Plural Noun: ")
# adjective = input("Enter an Adjective: ")

# print("Feeling adventurous, I told the barber for a",adjective,"new look. His grin could curdle milk. Snip, snip... CRUNCH! Turns out, he clipped off a chunk of hair and a stray",nounSingular,".  He tried to cover it with a",nounPlural,".  Needless to say, I left looking like a startled poodle, not a",nounSingular)


"""Lists"""
friends = ["prince","yash","bipin","mahin","Priyanshu"] #list
'''Print full list'''
# print(friends)

'''Print particular item => list[index]'''
# print(friends[0])

'''print a list in range => list[start:end] *end not included* '''
# print(friends[1:4])


"""List Functions"""
lucky_number = [4, 8, 15, 16, 23, 42] #list2
friends = ["Kevin","Karen","Jim","Jim","Oscar","Toby"] #list1
'''add another list into one => list1.extend(list2)'''
# friends.extend(lucky_number)
# print(friends)

'''add a element to a list => list.append(element)'''
# friends.append("Ruchi")
# print(friends)

'''add a element to a specific position => list.insert(index,element)'''
# friends.insert(1, "Kelly");
# print(friends)

'''remove a element from a list => list.remove(element)'''
# friends.remove("Jim")
# print(friends)

'''remove every element out of list(empty list) => list.clear()'''
# friends.clear()
# print(friends)

'''remove a element => list.pop(index) *if no index remove the last one*'''
# friends.pop(0)
# print(friends)

'''check a certain element => list.index(element)'''
# print(friends.index("Kevin"))

'''count the occurance of a element => list.count(element)'''
# print(friends.count("Jim"))

lucky_number = [4, -8, 15, -16, 37, 56, 23, 42]
'''sorting a list => list.sort()'''
# lucky_number.sort()
# print(lucky_number)

'''reversing a list => list.reverse()'''
# lucky_number.reverse()
# print(lucky_number)

'''Copying a list => list2 = list.copy()'''
# numbers2 = lucky_number.copy()
# print(numbers2)


"""Tuples""" #tuples are immutable (values cannot be changed)
tup = (2,3)
# tup[0] = 10; #error
# print(tup)
'''list of tuples'''
newTup = [(2,3),(4,6),(6,9)]
# newTup[0] = (6,7) #no error as this is a element of list
# print(newTup)


"""Functions"""
# def say_hi(name, age):
#     print("Hello",name,"You are",age)

# say_hi("Mike", 35)
# say_hi("Lucy", 70)


"""If-Else"""
# is_male = True
# is_tall = False
#
# if is_male and is_tall:
#     print("You are a tall male")
# elif is_male and not(is_tall):
#     print("You are a short male")
# else:
#     print("You are either not male or tall or both")


"""if-else & comparison"""
# def max_num(num1, num2, num3):
#     if num1>num2 and num1>num3:
#         return num1
#     elif num2>num1 and num2>num3:
#         return num2
#     else:
#         return num3
#
# print(max_num(300,40,5))


"""Better Calculator"""
# num1 = float(input("Enter number 1: "))
# op = input("Enter the operator: ")
# num2 = float(input("Enter number 2: "))
#
# if op == "+":
#     print(num1 + num2)
# elif op == "-":
#     print(num1 - num2)
# elif op == "*":
#     print(num1*num2)
# elif op == "/":
#     print(num1/num2)
# else:
#     print("Invalid Operator")


"""Dictionaries => key: value pair"""
monthConversion = {
    "Jan": "January",
    "Feb": "February",
    "Mar": "March",
    "Apr": "April",
    "May": "May",
    "Jun": "June",
    "Jul": "July",
    "Aug": "August",
    "Sept": "September",
    "Oct": "October",
    "Nov": "November",
    "Dec": "December",
}
# print(monthConversion["Mar"]) #March
# print(monthConversion.get("Mar")) #March
# print(monthConversion.get("Luv")) #None
# print(monthConversion.get("Luv","Not a valid Key")) #Not a valid Key


"""While Loop"""
# i = 1
# while i<=10:
#     print(i)
#     i+=1

# print("Done with loop")


"""Building a Guessing game"""
secret_word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess!= secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter your guess: ").lower()
        guess_count += 1
    else:
        out_of_guesses = True
if out_of_guesses:
    print("Out of Guesses, You LOSE!")
else:
    print("You Win")





