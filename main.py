def creating_dict(file):
    cook_book = {}
    with open(file, 'r') as f:
        for line in f:
            name = line.rstrip()
            count = int(f.readline())
            cook_book[name] = [0] * count

            for i in range(count):
                string_ingredient = f.readline().strip().split(' | ')
                cook_book[name][i] = ({'ingredient_name': string_ingredient[0],
                                       'quantity': int(string_ingredient[1]),
                                       'measure': string_ingredient[2]})
            f.readline()

    return cook_book


path = 'recipes.txt'
print(creating_dict(path))
