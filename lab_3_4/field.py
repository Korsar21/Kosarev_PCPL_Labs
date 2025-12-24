# Пример:
goods = [
    {'title': 'Ковер', 'price': 2000, 'color': 'green'},
    {'title': 'Диван для отдыха', 'color': 'black'}
]
# field(goods, 'title') должен выдавать 'Ковер', 'Диван для отдыха'
# field(goods, 'title', 'price') должен выдавать {'title': 'Ковер', 'price': 2000}, {'title': 'Диван для отдыха', 'price': 5300}

def field(items, *args):
    assert len(args) > 0
    if len(args) == 1:
        for i in range (len(items)):
            if args[0] in items[i]:
                print(items[i][args[0]], end=' ')
    else:
        for i in range (len(items)):
            new_dict = {}
            for j in range (len(args)):
                if args[j] in items[i]:
                    new_dict[args[j]] = items[i][args[j]]
            print(new_dict, end=' ')

if __name__ == '__main__':
    field(goods, 'title')
    print(end="\n")
    field(goods, 'title', 'price')


    # Необходимо реализовать генератор