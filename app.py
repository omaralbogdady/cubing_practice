# Imports ---------------
from guizero import App, Text, Box, PushButton

# Variables -------------

# Functions -------------

# App -------------------
app = App(title="Cubing Practice Simulator")
app.bg = "light blue"

title = Text(app, text="Cubing Practice")

buttons = Box(app, layout="grid")
button_2_digit = PushButton(buttons, text="2-digit cubes", grid=[0, 0])

app.display()