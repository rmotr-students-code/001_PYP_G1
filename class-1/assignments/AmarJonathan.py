#First homework
from datetime import datetime


from decimal import *

#mutable function
def mutato(received_list, appended):
	received_list.append(appended)

#immutable function
def brand_of_potato(received_list, appended):
		new_brand = received_list[:]
		new_brand.append(appended)
		return new_brand

#Square upwards function
def squareUpwards(integer):
	squareDictionary = { }
	x = integer
	for y in range(1,x+1):
		squareDictionary[y] = y*y
	return squareDictionary
	
#String splice every 3 digits
def stringSplice(string1, string2):
	newstring = ''
	
	for x in range(len(string1)):
		if x % 3 == 0 and x != 0:
			newstring += string2
		
		newstring += string1[x]
	return newstring
		
#Charly Scam Fix, requires decimal import
def payments(owed=10, payments=3):
	print (Decimal(owed) / Decimal(payments))

#Length of string
def stringLength(string, n=2):
	if len(string) < n:
		return 'Invalid string'
		
	y = len(string)
	newString = string
	counter = 0
	counter2 = 1
	for x in string[0:y]:
		if string[counter:counter2] == ' ':
			counter += 1
			counter2 += 1
		else:
			newString = string[counter:y]
			break
	return string[counter:counter+n]
	
#Upper Case
def upperCase(string):
	return string.upper()

#Camel Case
def returnCamelCase(recievedString):
	splitString = recievedString.split()
	splitString[0] = splitString[0].lower()
	
	for x in range(1, len(splitString)):
		splitString[x] = splitString[x].capitalize()
	
	return ''.join(splitString)


#check prime
def check_prime(number):	
	for x in range(number):
		if x > 1:
			if number % x == 0:
				return False
	return True

#next prime
def next_prime(number):
	counter = number + 1
	while True:
		if check_prime(counter) != True:
			counter += 1
		else:
			return counter

#count occurences of something
def countOccurences(recievedList):
	newDictionary = { }
	print (recievedList)
	for x in recievedList:
		if x in newDictionary:
			newDictionary[x] += 1
		else:
			newDictionary[x] = 1
	return newDictionary
