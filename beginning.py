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


#DICTIONARIES

fDictionary = {'key1':'hello'}
sDictionary = {'key1':'hello', 'key2':'world'}
tDictionary = {'key1':[{'key2':'hello'},'list sting']}
gDictionary = {'key1':[1,2,{'key2':['nested string',{'key3':[1,2,['hello']]}]}]}

fIndexing = fDictionary['key1']
print(fIndexing)
sIndexing = sDictionary['key2']
print(sIndexing)
tIndexing = tDictionary['key1'][0]['key2']
print(tIndexing)
gIndexing = gDictionary['key1'][2]['key2'][1]['key3'][2]
print(gIndexing)


#TUPLES

#tuples are prettty much lists that are immutable (can't change). Everything else about them act the same as lists


#SETS

#Pretty much unordered lists that are distinct. Imagine running a SELECT DISTINCT query in SQL



#OPERATORS (BOOLEANS)

#  == is equal to
#  != is NOT equal to
#  > greater than
#  < less than
#  >= greater than or equal to
#  <= less than or equal to



