from bottle import post, request #Импорт фреймворка
import re
import pdb
from datetime import datetime
import json
import os

# Путь к файлу
FILE_PATH = 'data.json'

# Проверка вопроса на соответствие условиям
def is_valid_question(quest):
    return len(quest) > 3 and not quest.isdigit()


@post('/home', method='post')
def my_form():

    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    cur_date = datetime.now().strftime("%Y-%m-%d") # получение текущей даты


    if not mail or not quest or not username:
        return "Please fill in all fields"

    if not re.match(r"[a-zA-Z0-9\\+\\.\\_\\%\\-\\+]{1,256}" +
            "\\@" +
            "[a-zA-Z0-9][a-zA-Z0-9\\-]{0,64}" +
            "(" +
                "\\." +
                "[a-zA-Z0-9][a-zA-Z0-9\\-]{0,25}" +
            ")+", mail):#регулярное выражение для проверки почтового адреса
        return "Please enter a valid email address"
    
    # Загрузка данных из файла или создание нового, если он не существует
    if os.path.exists(FILE_PATH):
        with open(FILE_PATH, 'r') as file:
            data = json.load(file)
    else:
        data = {}

    # Проверка наличия почтового адреса в данных
    if mail not in data:
        data[mail] = []

    # Проверка вопроса и добавление его в список, если он удовлетворяет условиям
    if is_valid_question(quest) and quest not in data[mail]:
        data[mail].append(quest)
    else :
        return "Enter a valid question/quest already exists"

    # Запись обновленных данных обратно в файл
    with open(FILE_PATH, 'w') as file:
        json.dump(data, file)
        
    return f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date : {cur_date}"
    