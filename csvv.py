import csv


def read():
    with open('testdata.csv',encoding='UTF-8')as f:
        data = csv.reader(f)
        next(data)
        list = []
        for i in data:
            list.append(i)
            return list