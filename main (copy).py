from SchoolApi import SchoolApi
import Rsp
import Quiz
import Marble
from tkinter import *
import random
from datetime import datetime as dt
from datetime import timedelta as td

# Initialize Tkinter
window = Tk()
window.title("T-Bot Chatbot")
window.geometry("400x600")

# Functions for UI
def t_bot_say(text):
	chat_box.insert(END, "T-Bot: " + text + "\n")
	chat_box.see(END)

def handle_user_input():
	user_input = input_box.get()
	chat_box.insert(END, "User: " + user_input + "\n")
	input_box.delete(0, END)  # Clear the input box

	if "meal" in user_input:
		t_bot_say("Are you asking about meals? Alright!\n" + "  1) Today's meal\n" +
				  "  2) Tomorrow's meal\n" +
				  "  3) Enter a specific date (YYYYMMDD) to check")
		selector = int(input())
		if selector == 1:
			t_bot_say("Today's meal is!")
			params = {"MLSV_YMD": dt.now().strftime("%Y%m%d")}
		elif selector == 2:
			t_bot_say("Tomorrow's meal is!")
			params = {"MLSV_YMD": (dt.now() + td(1)).strftime("%Y%m%d")}
		elif selector == 3:
			t_bot_say("Which date do you want to know the meal for? (YYYYMMDD)")
			params = {
				"MLSV_YMD": str(input()),
			}
		else:
			t_bot_say("Invalid input!")

		t_bot_say(SchoolApi("mealServiceDietInfo", params).meal())

	elif "timetable" in user_input:
		t_bot_say("Are you looking for the timetable?")
		params = {
			"GRADE": str(input("Which grade are you : ")),
			"CLASS_NM": str(input("Do you know your class name? : "))
		}
		t_bot_say("I will provide the timetable, dear user\n" + "  1) Today's timetable\n" +
				  "  2) Tomorrow's timetable\n" +
				  "  3) Enter a specific date (YYYYMMDD) to check")
		selector = int(input())
		if selector == 1:
			t_bot_say("Do you want to know today's timetable?")
			params["ALL_TI_YMD"] = dt.now().strftime("%Y%m%d")
		elif selector == 2:
			t_bot_say("Do you want to know tomorrow's timetable?")
			params["ALL_TI_YMD"] = (dt.now() + td(1)).strftime("%Y%m%d")
		elif selector == 3:
			t_bot_say("Which date's timetable would you like to know? (YYYYMMDD)")
			params["ALL_TI_YMD"] = str(input())
		else:
			t_bot_say("Invalid input!")

		t_bot_say(SchoolApi("hisTimetable", params).time())

	# You can add similar handling for other functionalities here

	else:
		t_bot_say("T-Bot doesn't know how to do that. Type 'help' to learn more.")


# Create UI elements
chat_box = Text(window, wrap=WORD, width=40, height=20)
input_box = Entry(window, width=40)
send_button = Button(window, text="Send", command=handle_user_input)

# Pack UI elements
chat_box.pack(pady=10)
input_box.pack()
send_button.pack()

# Initial message
hi = ['Hello! I am your assistant chatbot T-Bot!', 'T-Bot here! ⌛', 'I have arrived 🚀 -T-Bot',
	  'Do you need help from T-Bot?']
t_bot_say(f"{random.choice(hi)}\n" + "Please enter the school name you are looking for!")

window.mainloop()  # Start Tkinter UI loop
