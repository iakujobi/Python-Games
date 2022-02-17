# Import libraries
import tkinter as tk
from tkinter import messagebox

# Save the user's response to a variable
answer = messagebox.askyesno("Question", "Will you go out w/ me?")

# Respond to message
if answer == True:
    messagebox.showinfo("Happy", "Yayyy!!!")
else:
    messagebox.showinfo("Sad", "You suck!")


# # Respond to message (with an evil twist!)
# if answer == True:
#     messagebox.showinfo("Happy", "Yayyy!!!")
# else:
#     # Add while loop to a 'No' Response. User will not be able to close it.
#     while True:
#         messagebox.showinfo("Sad", "You suck!")
