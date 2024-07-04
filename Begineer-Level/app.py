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
print(friends)

'''Print particular item => list[index]'''
print(friends[0])

'''print a list in range => list[start:end] *end not included* '''
print(friends[1:4])


"""List Functions"""
