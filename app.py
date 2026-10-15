# Imports ---------------
from guizero import App, Text, Box, PushButton, Slider

# Variables -------------
num_of_questions = 1

# Functions -------------
def digit_2_menu():
    menu.hide()
    two_digit_menu.show()

def start(digit_cube, num_o_questions):
    two_digit_menu.hide()
    two_digit_mode.show()
    # print(f"{digit_cube}-digit cubes with {num_of_questions} questions")

def slider_change(slider_value):
    global num_of_questions
    num_of_questions = slider_value

# App -------------------
app = App(title="Cubing Practice Simulator")
app.bg = "dark orange"

# Main Menu -------------
menu = Box(app)

title = Text(menu, text="Cubing Practice")

buttons = Box(menu, layout="grid")
button_2_digit = PushButton(buttons, text="2-digit cubes", grid=[0, 0], command=digit_2_menu)

# 2-digit Menu ----------
two_digit_menu = Box(app)
two_digit_menu.hide()

two_digit_title = Text(two_digit_menu, text="Two Digit Cubes")
empty_space = Text(two_digit_menu, text=" ")

num_of_questions_title = Text(two_digit_menu, text="Number of questions:")
num_of_questions_slider = Slider(two_digit_menu, start=1, end=20, step=1, command=slider_change)
start_button = PushButton(two_digit_menu, text="Start", command=start, args=[2, num_of_questions])

# 2-digit mode ----------
two_digit_mode = Box(app)
two_digit_mode.hide()

two_digit_question = Text(two_digit_mode, text="What is the cube root of: [NUMBER]?")

app.display()