from datetime import datetime


def filter_by_state(operation_list: list[dict[str, str | int]], state: str = "EXECUTED") -> list[dict[str, str | int]]:
    """
    Фильтрует список по значению ключа state
    :param operations_list:
    :param state:
    :return:ц
    """
    filtered_list = []
    for dict in operation_list:
        if dict["state"] == state:
            filtered_list.append(dict)
    return filtered_list


def sort_by_date(operations_list: list[dict[str, str]], reverse: bool = True) -> list[dict[str, str]]:
    """
    Сортирует список словарей по убыванию либо возрастанию даты
    :param operations_list:
    :param reverse:
    :return:
    """
    sorted_list = sorted(
        operations_list,
        key=lambda operation: datetime.strptime(operation["date"], "%Y-%m-%dT%H:%M:%S.%f"),
        reverse=reverse,
    )
    return sorted_list
