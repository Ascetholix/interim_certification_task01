from func import *


def command():
    print('add - добавить, search - поиск, read - чтение, save - сохранить')

def main():
    value = ''
    while(value != 'exit'):
        command()
        print('Введите действие или введите exit')
        value = input('> ')
        if(value=='add'): notes()
        if(value=='search'): search_notes()
        if(value=='read'): read_notes()
        if(value=='save'): notes()

if __name__ == '__main__':
    main()

