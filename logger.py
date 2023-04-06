from datetime import datetime as dt

def note_log(notes):
  time = dt.now().strftime('%D;%H:%M:%S')
  with open('log.csv', 'a') as file:
    file.write('{};{}\n'
               .format(time,notes))