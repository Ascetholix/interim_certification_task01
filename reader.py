def read():
    with open('log.csv', 'r') as file:
        print(file.read())

def search(value):
    with open('log.csv', 'r') as file:
        list = file.read().split('\n')
        for i in list:
            list1 = i.split(';')
            for j in list1:
                if value in j: print(i)