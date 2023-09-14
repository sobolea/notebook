import json


target = input('Введите заголовок заметки, которую хотите прочитать: ')
with open('notes.json', "r") as my_file:
        data = my_file.read()


datas = json.loads(data)
for note in datas['n']:
        if note["name"] == target:
            print(note['name'] +" " + note["body"] + " " + note["time"])