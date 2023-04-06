from func import *


def command():
    print('add - добавить')
    print('search - поиск')
    print('read - чтение')
    print('save - сохранить')

def main():
    value = ''
    while(value != 'exit'):
        command()
        value = input('Введите действие: ')
        if(value=='add'): notes()
        if(value=='search'): search_notes()
        if(value=='read'): read_notes()
        if(value=='save'): notes()
        else: print('Некоректно!!!\n'
                    'Введите действие или введите exit')

if __name__ == '__main__':
    main()

