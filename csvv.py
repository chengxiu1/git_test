import csv


def read():
    with open('testdata.csv',encoding='utf-8')as f:
        data = csv.reader(f)
        list = []
        next(data)
        for i in data:
            list.append(i)
            return list