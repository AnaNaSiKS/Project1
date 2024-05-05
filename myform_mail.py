import re

pattern = r"^a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9?\.)+a-z0-9*"

def check_mail(mail):
    return re.match(pattern, mail)