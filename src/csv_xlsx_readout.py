import csv
import pandas as pd

def csv_readout(file_path: str) -> list:
    '''Принимает на вход путь до .csv файла, возвращает список транзакций'''
    if file_path.endswith('.csv'):
        with open(file_path) as file:
            reader = csv.DictReader(file, delimiter=";")
            next(reader)
            transactions_list = []
            for row in reader:
                transactions_list.append(row)
        return transactions_list

def xlsx_readout(file_path: str) -> list:
    '''Принимает на вход путь до .xlsx файла, возвращает список транзакций'''
    df = pd.read_excel(file_path)
    transactions_list = df.to_dict(orient="records")
    return transactions_list
