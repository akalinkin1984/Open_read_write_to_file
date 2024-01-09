def creating_dict():
    cook_book = {}
    with open('recipes.txt', 'r') as f:
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


print(creating_dict())


def get_shop_list_by_dishes(dishes: list, person_count: int):
    result_dict = {}
    cook_book = creating_dict()
    for dish in dishes:
        for value in cook_book[dish]:
            ingredient = value['ingredient_name']
            measure = value['measure']
            quantity = value['quantity']
            if ingredient in result_dict:
                result_dict[ingredient]['quantity'] += quantity * person_count
            else:
                result_dict[ingredient] = {'measure': measure, 'quantity': quantity * person_count}

    return result_dict


print(get_shop_list_by_dishes(['Фахитос', 'Омлет'], 3))
