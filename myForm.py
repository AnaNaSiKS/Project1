from bottle import post, request #Импорт фреймворка
import re
import pdb
from datetime import datetime

@post('/home', method='post')
def my_form():
    questions = {}
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
    
    questions[mail] = quest
    pdb.set_trace()

    return f"Thanks, {username}! The answer will be sent to the mail {mail}. Access Date : {cur_date}"
    