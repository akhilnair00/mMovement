import sys
import customtkinter as ctk
import pyautogui
import random
import time
import easygui

# Last Updated: 3/7/2023;
# Breaks if you click the CustomTkinter GUI. Not sure why but just don't click it. Maybe I'll fix it in the future.




# pyautogui failsafe that would destroy everything if it didn't work
pyautogui.FAILSAFE = True

# creating CTkinter instance
rootCtk = ctk.CTk()
rootCtk.geometry("700x240")
rootCtk.title("MMovement v1.0 - anair")

# creating nice little icon!
rootCtk.iconbitmap("MouseIcon.ico")

# Shitty method to break out of the program... barely works
def breakMovement():
    sys.exit()


def beginMovement():
    count = 0
    totalTime = easygui.integerbox("Enter total runtime(in seconds)", lowerbound=0, upperbound=500)
    print(totalTime)
    while count != totalTime:
        x = random.randint(0, 1920)
        y = random.randint(0, 1080)
        pyautogui.moveTo(x, y, 0.5)
        pyautogui.scroll(10)
        print(pyautogui.position())
        time.sleep(5)
        count += 1
        print(count)


# Label indicating failsafe
label = ctk.CTkLabel(master=rootCtk, text="To naturally cancel mouse movement, please move mouse pointer to the top "
                                          "left corner of "
                                          "screen in between movement", corner_radius=8)
label.place(relx=0.5, rely=0.1, anchor=ctk.CENTER)

# Begins the mouse movement
button = ctk.CTkButton(master=rootCtk, text="Begin Movement", corner_radius=10, command=beginMovement)
button.place(relx=0.5, rely=0.5, anchor=ctk.CENTER)

# Attempts to end the mouse movement
button2 = ctk.CTkButton(master=rootCtk, text="Force Stop (Will take time and cause a crash)", corner_radius=10,
                        command=breakMovement)
button2.place(relx=0.5, rely=0.8, anchor=ctk.CENTER)

rootCtk.mainloop()

# STALLED: Slider is nice, but it doesn't allow proper fine-tuning, would much rather there be a textbox
#   slid = ctk.CTkSlider(master=rootCtk, from_=0, to=500, command=timeJig, hover=True)
#   slid.place(relx=0.5, rely=0.65, anchor=ctk.CENTER)


# STALLED: It instantly passes the value to beginMovement rather than just storing the input, it's annoying
# def timeJig(number):
#    print("Total Time: ", number)
#    return number
