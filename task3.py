import time
cook_book = {}

def logger(old_function):

    def new_function(*args, **kwargs):
        data_func = []
        time_func = f'время вызова - {time.ctime()}'
        name_func = f'имя - {old_function.__name__}'
        argument = f'аргументы - {*args, kwargs}'
        result = old_function(*args, **kwargs)
        res = f'возвращаемое значение - {result}'
        data_func.append(time_func)
        data_func.append(name_func)
        data_func.append(argument)
        data_func.append(res)
        data_func = str(data_func)
        with open('main3.log', 'a', encoding='UTF-8') as f:
            f.write(data_func)
        return result
    return new_function

@logger
def get_shop_list_by_dishes(dishes, person_count):
    shop_list_by_dishes = {}
    for dish in dishes:
        if dish in cook_book.keys():
            for comp in cook_book[dish]:
                ingr_name = comp['ingredient_name']
                mes = comp['mesuare']
                quan = int(comp['quantity']) * person_count
                if ingr_name in shop_list_by_dishes.keys():
                    shop_list_by_dishes[ingr_name]['quantity'] += quan
                else:
                    shop_list_by_dishes[ingr_name] = {'mesuare': mes, 'quantity': quan}
        else:
            print(f'Блюда {dish} нет')
    return shop_list_by_dishes

get_shop_list_by_dishes('салат', 5)