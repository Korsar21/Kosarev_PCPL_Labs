from operator import itemgetter

class Column:
    def __init__(self, id: int, id_table: int, name: str, type: str):
        self.id = id
        self.id_table = id_table
        self.name = name
        self.type = type

class Table:
    def __init__(self, id: int, name: str):
        self.id = id
        self.name = name

class TablesToColumns:
    def __init__(self, table_id: int, column_id: int):
        self.table_id = table_id
        self.column_id = column_id


if __name__ == "__main__":
    table_1 = Table(1,"Таблица 1")
    table_2 = Table(2,"Таблица 2")
    table_3 = Table(3,"Таблица 3")
    table_4 = Table(4,"Таблица 4")

    column_1 = Column(1,3,"Колонка сомов","Целое")
    column_2 = Column(2,2,"Колонка кружков","Целое")
    column_3 = Column(3,2,"Колонка 3","Целое")
    column_4 = Column(4,1,"Колонка крючков","Целое")
    column_5 = Column(5,1,"Колонка завозов","Целое")
    column_6 = Column(6,1,"Колонка 6","Целое")

    tab_to_col_1 = TablesToColumns(3, 1)
    tab_to_col_2 = TablesToColumns(2, 2)
    tab_to_col_3 = TablesToColumns(2, 3)
    tab_to_col_4 = TablesToColumns(1, 4)
    tab_to_col_5 = TablesToColumns(1, 5)
    tab_to_col_6 = TablesToColumns(1, 6)

    tables: list[Table] = [table_1, table_2, table_3, table_4]
    columns: list[Column] = [column_3, column_2, column_1, column_6, column_5, column_4]
    tab_to_col: list[TablesToColumns] = [tab_to_col_3, tab_to_col_2, tab_to_col_1, tab_to_col_6, tab_to_col_5, tab_to_col_4]

    # Первый запрос
    one_to_many = []
    for i in range (len(tables)):
        for j in range (len(columns)):
            if tables[i].id == columns[j].id_table:
                one_to_many.append((tables[i].id, tables[i].name, columns[j].id, columns[j].name))

    result_1 = sorted(one_to_many, key=itemgetter(2))
    print("Задание 1: ", result_1)

    # Второй запрос
    table_to_amount = []
    for i in range (len(tables)):
        amount_columns: int = 0
        for j in range (len(columns)):
            if tables[i].id == columns[j].id_table:
                amount_columns += 1
        table_to_amount.append((tables[i].id, amount_columns))

    result_2 = sorted(table_to_amount, key=itemgetter(1))
    print("Задание 2: ", result_2)

    # Третий запрос
    dictionary = dict()
    many_to_many_1 = []
    for i in range (len(tables)):
        for j in range (len(tab_to_col)):
            if tables[i].id == tab_to_col[j].table_id:
                many_to_many_1.append((tables[i].id, tables[i].name, tab_to_col[j].column_id))

    many_to_many_2 = []
    for i in range(len(many_to_many_1)):
        for j in range(len(columns)):
            if many_to_many_1[i][2] == columns[j].id:
                many_to_many_2.append((many_to_many_1[i][0], many_to_many_1[i][1], many_to_many_1[i][2], columns[j].name))



    for i in range (len(tables)):
        array_columns = []
        for j in range (len(many_to_many_2)):
            if tables[i].id == many_to_many_2[j][0] and many_to_many_2[j][3][-2:] == 'ов':
                array_columns.append(many_to_many_2[j][3])
        if len(array_columns) > 0:
            dictionary[tables[i].name] = array_columns

    print("Задание 3: ", dictionary)