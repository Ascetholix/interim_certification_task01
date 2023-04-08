from func import *


def command():
    print('add - добавить, search - поиск, read - чтение')
    print('save - сохранить, edit - редактировать, del - удалять')

def main():
    value = ''
    while(value != 'exit'):
        command()
        print('Введите действие или введите exit')
        value = input('> ')
        if(value=='add'): notes()
        if(value=='search'): search_notes()
        if(value=='read'): read_notes()
        if(value=='edit'): edit_notes()
        if(value=='del'): del_notes()

if __name__ == '__main__':
    main()

