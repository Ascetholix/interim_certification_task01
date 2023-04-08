from logger import *
from reader import *

def search_notes():
    value = input('Поиск > ')
    print(search(value))

def notes():
    value = input("Введите заметку > ")
    creat_log(value)
    print("Заметка успешно сохранена\n")

def read_notes():
    read_log()

def edit_notes():
    value = input("Введите заметку > ")
    text = search(value)
    print(text)
    edit_text(text)

def del_notes():
    value = input("Введите заметку > ")
    text = search(value)
    del_text(text)
