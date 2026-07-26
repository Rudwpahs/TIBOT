import os
from tkinter import *
def dobby_say(msg):
    print("TiBot: " + msg)


def answer():
    return input("User: ")

def petc():  #press enter to continue
    print()
    input("Press Enter to continue...")
#while문 사용시 clear로 인해 텍스트가 사라지는걸 방지하는 함수

def clear():
    command = 'clear'
    if os.name in ('nt', 'dos'):  # If Machine is running on Windows, use cls
        command = 'cls'
    os.system(command)