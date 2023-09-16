import math


# ORDER OF OPERATIONS

print('Hello world')
print(4 * (6 + 5))
print(4 * 6 + 5)
print(4 + 6 * 5)


#MATH

#square root
print(math.sqrt(4))
#power function/ squared
print(pow(2, 2))
#power funciton, to the 3rd
print(pow(2,3))


#STRINGS

s = 'hello'
result = s.index('e')
print(result)
print(s[1])
print(s[4])
print(s[len(s)-1])


#LISTS

#creating list
fList = [0,0,1]
sList = ['First', 'Second', 'Third']
print(sList)
#changing part of list
sList[2] = ['Nested', 1]
print(sList)

#List loop
addList = [2,3,4,5]
for i in range(len(addList)):
    fList.append(addList[i])
    print(fList)

#Sort list
fList.sort(reverse=True)
print(fList)
