# can create a class-like immutable object as a named tuple

from collections import namedtuple

Duck = namedtuple('Duck', 'color bill tail')

duck1 = Duck('green', 'yellow', 'short')
duck2 = Duck(bill='gnarly', tail='long', color='red')

# duck1.color = 'green'
# duck1.bill = 'yellow'
# duck1.tail = 'short'

print(duck1.color)
print(duck1.bill)
print(duck1.tail)
# print(duck1.thing)

# duck1.tail = 'long'
# print(duck1.color)
# print(duck1.bill)
# print(duck1.tail)

print(duck2.color)
print(duck2.bill)
print(duck2.tail)
