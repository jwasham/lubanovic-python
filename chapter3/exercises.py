"""
Exercises from chapter 3 for review
"""


def main():
    birth_year = 1971
    years = 5
    years_list = [y for y in range(birth_year, birth_year + years + 1)]

    print("Year born: ", years_list[0])
    print("Third birthday: ", years_list[3])
    print("Last year:", years_list[-1])

    things = ['mozzarella', 'cinderella', 'salmonella']
    things[1] = things[1].capitalize()
    things[0] = things[0].upper()
    del things[-1]
    print(things)

    surprise = ['Groucho', 'Chico', 'Harpo']
    surprise[-1] = surprise[-1].lower()
    surprise[-1] = surprise[-1][::-1]
    surprise[-1] = surprise[-1].capitalize()
    print(surprise)

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

if __name__ == '__main__':
    main()
