
import random
import string

def stud_key():

    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def teach_key():

    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def class_id():

    return ''.join(random.choices(string.ascii_letters + string.digits, k=10))

def content_id():

    return ''.join(random.choices(string.ascii_letters + string.digits, k=15))
