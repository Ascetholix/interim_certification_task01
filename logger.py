from datetime import datetime as dt

def creat_log(notes):
  time = dt.now().strftime('%D;%H:%M:%S')
  with open('log.csv', 'a') as file:
    file.write('{};{}\n'
               .format(time,notes))

def read_log():
    with open('log.csv', 'r') as file:
        print(file.read())

def save_log(notes):
    with open('log.csv', 'a') as file:
        file.write('{}\n'
                   .format(notes))

def clear_log():
    with open('log.csv', 'w') as file:
        file.write('{}'
                   .format(''))