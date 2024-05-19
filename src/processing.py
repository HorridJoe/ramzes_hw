from datetime import datetime

def filter_by_state(operations_list, state: str = 'EXECUTED') -> list:
    '''
    Фильтрует список по значению ключа state
    :param operations_list:
    :param state:
    :return:
    '''
    filtered_list = []
    for dict in operations_list:
        if dict['state'] == state:
            filtered_list.append(dict)
    return filtered_list

def sort_by_date(operations_list, reverse: bool = True) -> list:
    '''
    Сортирует список словарей по убыванию либо возрастанию даты
    :param operations_list:
    :param reverse:
    :return:
    '''
    sorted_list = sorted(
    operations_list,
    key=lambda operation: datetime.strptime(operation['date'], '%Y-%m-%dT%H:%M:%S.%f'),
    reverse=reverse
    )
    return sorted_list
