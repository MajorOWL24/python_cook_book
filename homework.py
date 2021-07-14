def read_recipes(filename):
    f = open(filename, encoding='utf-8', newline='\n')

    state = 1
    i = 0
    k = 0
    name = ''

    book = {}
    for line in f:
        line = line.strip()
        if state == 1 and len(line) > 0:
            # dish name
            name = line
            book[name] = []
            state = 2
        elif state == 2:
            # ingridients count
            k = int(line)
            i = 0
            state = 3
        elif state == 3:
            # ingridient
            data = line.split(' | ')
            book[name].append({
                'ingridient_name': data[0],
                'quantity': int(data[1]),
                'measure': data[2]
            })
            i = i + 1
            if i == k:
                state = 1
    return book


cook_book = read_recipes('recipes.txt')


def get_shop_list_by_dishes(dishes, person_count):
    data = {}
    for dish in dishes:
        for ingridient in cook_book[dish]:
            if ingridient['ingridient_name'] not in data:
                data[ingridient['ingridient_name']] = {'measure': ingridient['measure'], 'quantity': 0}
            data[ingridient['ingridient_name']]['quantity'] += ingridient['quantity'] * person_count
    return data
