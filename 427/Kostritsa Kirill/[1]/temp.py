towns = ["Большая Пысса", "Большие Пупсы", "Манды", "Дешевки", "Такое",
         "Тухлянка", "Баклань", "Лохово", "Факфак", "Большое Струйкино",
         "Овнище", "Дно", "Трусово", "Косяковка", "Куриловка", "Ширяево",
         "Ломки", "Большой Куяш", "Иннах", "Крутые Хутора", "Крутая", "Новые Алгаши" 
         "Новопозорново", "Болотная Рогавка", "Старые Черви", "Верхнее Зачатье", 
         "Дураково", "Козявкино", "Цаца", "Засосная", "Муходоево", "Да-да", "Хреновое",
         "Блювиничи", "Большое Бухалово", "Свиновье", "Синие Лепяги", "Жабино"]

dict_towns = {}
for i in range(len(towns)):
    dict_towns[towns[i]] = i

def column_print(dict_towns):
    print(">>")
    for x in dict_towns:
        print(x)
    print("<<")

def del_name(dict_towns):
    print("\nВведите название города, который хотите удалить:")
    town = str(input())
    print("После удаления:")
    dict_towns.pop(town)
    column_print(dict_towns)

def add_word(dict_towns):
    print("\nВведите номер места, куда хотите добавить слово \"Конец\":")
    index = int(input())
    word = "Конец"
    
    items = list(dict_towns.items())
    items.insert(index, (word, index))
    dict_towns = dict(items)
    print("Список после добавления:")
    column_print(dict_towns)
    
dict_towns = dict(sorted(dict_towns.items(), key=lambda x:x[1]))

column_print(dict_towns)
del_name(dict_towns)
add_word(dict_towns)