#Задача 1
print ('Задача #1')
with open('recipes.txt', encoding='utf-8') as file:
    cook_book = {}
    for i in file:
        recipe_name = i.strip()
        ingredients_count = file.readline()
        ingredients = []
        for p in range(int(ingredients_count)):
            recipe = file.readline().strip().split(' | ')
            ingredient_name, quantity, measure = recipe
            ingredients.append({'ingredient_name': ingredient_name, 'quantity': quantity, 'measure': measure})
        file.readline()
        cook_book[recipe_name] = ingredients
print(cook_book)

#Задача 2
print ('Задача #2')
def get_shop_list_by_dishes(person_count: int, dishes: list):
    result = {}
    for dish in dishes:
        if dish in cook_book:
            for consist in cook_book[dish]:
                if consist['ingredient_name'] in result:
                    result[consist['ingredient_name']]['quantity'] += int(consist['quantity'])  * person_count
                else:
                    result[consist['ingredient_name']] = {'measure': consist['measure'],'quantity': int(consist['quantity']) * person_count}
        else:
            print('Такого блюда нет в книге')
            
    return result
    
print(get_shop_list_by_dishes(2, ['Запеченный картофель', 'Омлет']))
