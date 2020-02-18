import itertools #bron: https://stackoverflow.com/questions/47380999/how-to-make-a-list-with-all-possible-combinations

def possibilities():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']
    possibilities = []

    for i in itertools.product(lst, repeat=4):
        possibilities.append(i)

    possibilities.sort()
    return possibilities
