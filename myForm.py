from bottle import post, request #Импорт фреймворка
import re
from datetime import datetime

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')
    username = request.forms.get('USERNAME')
    cur_date = datetime.now().strftime("%Y-%m-%d") # получение текущей даты


    if not mail or not quest or not username:
        return "Please fill in all fields"

    if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):#регулярное выражение для проверки почтового адреса
        return "Please enter a valid email address"

    return f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date : {cur_date}"
