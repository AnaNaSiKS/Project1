from bottle import post, request
import re

@post('/home', method='post')
def my_form():
    mail = request.forms.get('ADRESS')
    quest = request.forms.get('QUEST')

    if not mail or not quest:
        return "Please fill in all fields"

    if not re.match(r"[^@]+@[^@]+\.[^@]+", mail):
        return "Please enter a valid email address"

    return "Thanks! The answer will be sent to the mail %s" % mail
