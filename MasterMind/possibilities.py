import itertools #bron: https://stackoverflow.com/questions/47380999/how-to-make-a-list-with-all-possible-combinations

def possibilities():
    lst = ['R', 'B', 'G', 'Y', 'P', 'W']
    possibilities = []

    for i in itertools.product(lst, repeat=4):  # creates an list of tuples with the lenght with all the possibilities
        possibilities.append(i)                 # from the list of colours.

    possibilities.sort()
    return possibilities

