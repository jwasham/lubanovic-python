import re

title = 'Young Frankenstein'

m1 = re.match('You', title)
if m1:
    print(m1.group())

m2 = re.match('Frank', title)
if m2:
    print(m2.group())
else:
    print("Did not match from beginning")

# match() only matches at beginning, case sensitive

m3 = re.search('Frank', title)
if m3:
    print(m3.group())
else:
    print("Did not find it anywhere")

m4 = re.match('.*Frank', title)
if m4:
    print(m4.group())
else:
    print("Did not find with star")

m5 = re.findall('n.?', title)
if m5:
    print(m5)
else:
    print("Did not find any")

print(re.split('n', title))

print(re.sub('n', 'X', title))  # sub = replace



