import csv


def read():
    with open('csvv.py',encoding='utf-8')as f:
        data = csv.reader(f)
        next(data)
        list = []
        for i in data:
            list.append(i)
            return list