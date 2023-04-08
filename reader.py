from logger import *

def list_note():
    with open('log.csv', 'r') as file:
        list = file.read().split('\n')
        return list


def search(value):
    list = list_note()
    b = True
    for i in list:
        list1 = i.split(';')
        for j in list1:
            j = j.lower()
            if value in j:
                b = False
                return i
    if b:
        return 'Нет результата'

def del_text(value):
    list = list_note()
    b = False
    for i in list:
        if value == i:
           list.remove(i)
           b = True
    if b:
        clear_log()
        for i in list:
           save_log(i)

def edit_text(value):
    text = input("Введите новую заметку > ")
    list = list_note()
    b = False
    for i in list:
        if value == i:
            index = list.index(i)
            list1 = i.split(';')
            list1.pop(-1)
            list1.insert(len(list1), text)
            tmp = list1[0]+";"+list1[1]+";"+list1[2]
            list.pop(index)
            list.insert(index,tmp)
            b = True
            print(tmp)
        if b:
            clear_log()
            for i in list:
                save_log(i)
