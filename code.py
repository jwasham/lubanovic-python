name = 'Hello there everybody'
print(name.upper())
print(name.endswith('body'))
print(name.isalpha())
print(name.swapcase())
print(name[3:9])

theList = []
print(theList)

anotherList = list()
print(anotherList)

letters = list('hello')
print(letters)

birthday = '12/26/1971'
print(birthday.split('/'))

otherName = list('Wanda')
otherName[2] = 'f'
print(''.join(otherName))

newList = ['one', 'two', 'three']
print(newList)

print(newList[0:1])

reversedList = newList[::-1]
print(reversedList)

reversedList.append('zero')
print(reversedList)

arr1 = ['i1', 'i2']
arr2 = ['i3', 'i4']

arr3 = arr1 + arr2
print(arr3)

del(arr3[-1])
print(arr3)

arr3.remove('i2')
print(arr3)

more = ['i5', 'i6']

arr3 += more

print(arr3.pop())
print(arr3.pop(1))

print(arr3)

print('i3' in arr3)
print('i1' in arr3)

print(arr3.index('i5'))

names = ['Joe', 'Max', 'Scott', 'Brian']
print('sorted:', sorted(names))
print('unsorted:', names)
names.sort()  # sort in place
print('internal sort', names)

print(len(names))

arr = [1, 2, 3]
print(arr)

anotherArr = arr
anotherArr[1] = 'two'

# same reference
print(arr)
print(anotherArr)

newArr = [1, 2, 3]
copyArr = newArr.copy()
copyArr[1] = 'two'

print(newArr)

a, b, c = copyArr

print(b)

dicty = {
    "name": "John",
    "address": "788 110th Ave NE",
    "apt": "N1405",
}

print(dicty['name'])

myDict = {}
myDict['name'] = 'Joe'
myDict['birthdate'] = '2/14/1984'
print(myDict)

newInfo = {
    'birthdate': '3/14/1984',
}

print("updating")

myDict.update(newInfo)
print(myDict)

nameInDict = 'name' in myDict
ageInDict = 'age' in myDict

print(nameInDict)
print(ageInDict)

val = myDict.get('name', False)

print(val)

# python returns list
# python3 returns dict_keys()
print(myDict.keys())
print(myDict.values())
print(myDict.items())

dictCopy = myDict.copy()
print(myDict.keys())

drinks = {
    'martini': {'vodka', 'vermouth'},
    'black russian': {'vodka', 'kahlua'},
    'white russian': {'cream', 'kahlua', 'vodka'},
    'manhattan': {'rye', 'vermouth', 'bitters'},
    'screwdriver': {'orange juice', 'vodka'}
}

for drink, ingredients in drinks.items():
    if 'vodka' in ingredients:
        print('has vodka:', drink)

testList = ['one', 'capme', 'three']
upperStr = testList[1].upper()
print(upperStr)

e2f = {
    'dog': 'chien',
    'cat': 'chat',
    'walrus': 'morse'
}

print(e2f['walrus'])

f2e = {}

for eng, fr in e2f.items():
    f2e[fr] = eng

print(f2e['morse'])

print('===== logic =====')

foo = 1
if foo:
    print("we got foo")

count = 1
while count <= 5:
    print(count)
    count += 1

print('===== while loop with input and break =====')

# while True:
#     value = input("type a word to capitalize [q or enter to exit]: ")
#     if value == 'q' or value == '':
#         print('All done.')
#         break
#     else:
#         print(value.capitalize())

print('===== hitting else when break wasn\'t hit =====')

numbers = [1, 3, 5]
position = 0
length = len(numbers)
while position < length:
    number = numbers[position]
    if number % 2 == 0:  # even
        print('Found even number: ', number)
        break
    position += 1
else:
    print('No even numbers found')

print('===== list comprehension =====')

rows = range(5, 10)  # last in range is never reached. it's y - 1
cols = range(1, 5)
cells = [(row, col) for row in rows for col in cols if row % 2 == 0]  # even rows only

# unpack
for row, col in cells:
    print("row:", row, "col:", col)

print('===== dictionary comprehension =====')

word = 'letters'
letterCounts = {letter: word.count(letter) for letter in word}
print(letterCounts)

print('===== functions =====')


def dinner(wine, entree, dessert):
    return {'wine': wine, 'entree': entree, 'dessert': dessert}

print(dinner(dessert='pie', wine='malbec', entree='steak'))

# Using * with arguments


def my_func(*args):
    """returns an arg list"""
    return args

print(my_func('me', 'myself', 'I'))


def my_other_func(**kwargs):
    return kwargs

print(my_other_func(self='me', other='myself', other2='I'))

