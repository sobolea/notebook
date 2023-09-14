'''Реализовать консольное приложение заметки, 
с сохранением, чтением, добавлением, 
редактированием и 
удалением заметок. Заметка должна
содержать идентификатор, заголовок, тело заметки и дату/время создания или последнего изменения заметки. Сохранение заметок необходимо сделать в
формате json или csv формат (разделение полей рекомендуется делать через точку с запятой). Реализацию пользовательского интерфейса студент может
делать как ему удобнее, можно делать как параметры запуска программы (команда, данные), можно делать как запрос команды с консоли и
последующим вводом данных, как-то ещё, на усмотрение студента.Например:
python notes.py add --title "новая заметка" –msg "тело новой заметки"
Или так:
python note.py
Введите команду: add
Введите заголовок заметки: новая заметка
Введите тело заметки: тело новой заметки
Заметка успешно сохранена
Введите команду: 
При чтении списка заметок реализовать фильтрацию по дате.
'''

import os
from datetime import datetime
import json

def show_notes(file_name):
    os.system('CLS')
    with open(file_name, "r") as my_file:
        data = my_file.read()
    datas = json.loads(data)
    sorted_date = sorted(datas['n'], key=lambda x: datetime.strptime(x["time"], '%H:%M:%S'))
    for note in sorted_date:
        print(note['name'] +" " + note["body"] + " " + note["time"])
    input('\npress any key ')

def add_note(file_name, id):
    now = datetime.now()
    if id == 0:
        data = {}
        data['n'] = []
        # data = []
        data['n'].append({
        # data.append({
            'id' : id,
            'name' : input('Введите заголовок заметки: '),
            'body' : input('Введите тело заметки: '),
            'time' : now.strftime("%H:%M:%S")
        })
        with open(file_name, 'w') as f:
           json.dump(data, f)
    else:
        
        with open(file_name, 'r') as f:
            data = json.load(f)
        new_note = [{
            'id' : id,
            'name' : input('Введите заголовок заметки: '),
            'body' : input('Введите тело заметки: '),
            'time' : now.strftime("%H:%M:%S")
        }]
        data['n']+= new_note

        with open(file_name, 'w') as f:
            json.dump(data, f)
    print("Заметка успешно сохранена")

def read_note(file_name):
    flg = False
    target = input('Введите заголовок заметки, которую хотите прочитать: ')
    os.system('CLS')
    with open('notes.json', "r") as my_file:
        data = my_file.read()
    datas = json.loads(data)
    for note in datas['n']:
        if note["name"] == target:
            flg = True
            print(note['name'] +" " + note["body"] + " " + note["time"])
    if flg == False:
        print("no notes with this name")
    input('\npress any key ')

def change_note(file_name):
    flg = False
    now = datetime.now()
    target = input('Введите заголовок заметки, которую хотите редактировать: ')
    with open(file_name, "r") as my_file:
        data = my_file.read()
    datas = json.loads(data)
    for note in datas['n']:
        if note["name"] == target:
            flg = True
            note["name"] = input('Input name: ')
            note["body"] = input('Input body: ')
            note["time"] = now.strftime("%H:%M:%S")
            with open(file_name, "w") as my_file:
                my_file.write(json.dumps(datas))
    if flg == False:
        print("no notes with this name")
    print("Заметка успешно изменена")
    input('\npress any key ')

def delete_note(file_name):
    flg = False
    target = input('Введите заголовок заметки, которую хотите удалить: ')
    with open(file_name, "r") as my_file:
        data = my_file.read()
    datas = json.loads(data)
    for note in datas['n']:
        if note["name"] == target:
            flg = True
            del datas['n'][note["id"]]
        with open(file_name, "w") as my_file:
            my_file.write(json.dumps(datas))
    if flg == False:
        print("no notes with this name")
    print("Заметка успешно удалена")
    input('\npress any key ')

def drawing():
    print('1 - show notes')
    print('2 - add note')
    print('3 - read note')
    print('4 - delete note')
    print('5 - change note')
    print('6 - exit')

def main(file_name, id):
    while True:
        drawing()
        user_choice = int(input('input a number from 1 to 6: '))
        os.system('CLS')
        if user_choice == 1:
            show_notes(file_name)
            os.system('CLS')
        elif user_choice == 2:
            add_note(file_name, id)
            id +=1
            os.system('CLS')
        elif user_choice == 3:
            read_note(file_name)
            os.system('CLS')
        elif user_choice == 4 :
            delete_note(file_name)
            os.system('CLS')
        elif user_choice == 5:
            change_note(file_name)
            os.system('CLS')
        elif user_choice ==6 :
            print('have a nice day')
        
            return

id = 0
os.system('CLS')
main('notes.json', id)