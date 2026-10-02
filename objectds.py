mystring = "new string"

print(mystring[::-1]) # reverses the string


# string concatenation

string1 = "Hello"
string2 = "World"

print(string1 + " " + string2) # concatenates the two strings with a space in between



print("2" + "3")     

print(string1.upper())

string3 = "HELLO HI"    
print(string3.lower())

print(string3.split()) # splits the string into a list 

# String formatting

name = "John"
age = 30

print(f'my name is {name} and age is {age}')

#LIST


square = [1, 4, 9, 16, 25]

print(square[0])

print(square + [21,1])

print(square.append(36))
print(square)

list1 = [1, 2, 3]

list2 = list1

print(id(list1) == id(list2)) # True, both list1 and list2 point to the same object in memory

list2.append(4)

print(list1) # [1, 2, 3, 4], list1 is also modified because list2 is a reference to the same object


print(len(list1)) # 4, the length of list1 is now 4 after appending an element to list2


twoDarray = [[1, 2, 3], [4, 5, 6]]
print(twoDarray[0][1])


