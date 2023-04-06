from logger import *
from reader import *

def search_notes():
    value = input('Поиск > ')
    search(value)

def notes():
    value = input("Введите заметку > ")
    note_log(value)
    print("Заметка успешно сохранена\n")

def read_notes():
    read()