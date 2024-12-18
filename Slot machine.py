#Declaring all imports up here as well as shortening for efficiency.
import os as o
import time as t
import tkinter as tk
from tkinter import font
import random as r

#Creating the root widget for tkinter as well as the font that is used (Mainly used for size)
root = tk.Tk(className="Lucky slots!")
large_font = font.Font(family="Helvetica", size=20, weight="bold")


#Declaring global variables
global counter
global counter_spin
global slot
global stop_coloumn_0
global stop_coloumn_1
global stop_coloumn_2
global spun
global spins
global locked

#Declaring tkinter labels as global
global row_1_label
global row_2_label
global row_3_label
global row_4_label
global row_5_label
global spin_button

#Declaring each coloumn save point
global coloumn_0_0
global coloumn_1_0
global coloumn_2_0
global coloumn_3_0
global coloumn_4_0
global coloumn_0_1
global coloumn_1_1
global coloumn_2_1
global coloumn_3_1
global coloumn_4_1
global coloumn_0_2
global coloumn_1_2
global coloumn_2_2
global coloumn_3_2
global coloumn_4_2

#Assigning values
coloumn_0_0 = ""
coloumn_1_0 = ""
coloumn_2_0 = ""
coloumn_3_0 = ""
coloumn_4_0 = ""
coloumn_0_1 = ""
coloumn_1_1 = ""
coloumn_2_1 = ""
coloumn_3_1 = ""
coloumn_4_1 = ""
coloumn_0_2 = ""
coloumn_1_2 = ""
coloumn_2_2 = ""
coloumn_3_2 = ""
coloumn_4_2 = ""

#More assignment
counter_spin = 0
counter = 0
spins = 999
spun = False
locked = False
stop_coloumn_0 = False
stop_coloumn_1 = False
stop_coloumn_2 = False
slot = [["| 👻|","| 💲 |","| 💩|"], #Slot dictionary used to keep track of the slots and aid in movement of each row
            ["| 💲 |","| 🍒|","| 💲 |"],
            ["| 🏹|","| 💩|","| 🏹|"],
            ["| 🍒|","| 🏹|","| 👻|"],
            ["| 💩|","| 👻|","| 🍒|"]]

def randomize_odds(): #Function to create random odds (Jackpot is not precalculated)
    global spun #Declaring globals used in the program
    global counter_spin
    global spins
    global locked
    locked = False #Whenever called unlock the odds
    if spun == True and counter_spin <= 10 and locked == False:
        spins = r.randint(132,314) #Generate a value from 132 to 314
        locked = True #Lock the odds

def spin():
    #Declare globals used within the function
    global row_1_label
    global row_2_label
    global row_3_label
    global row_4_label
    global row_5_label
    global spin_button
    global counter
    global counter_spin
    global slot
    global stop_coloumn_0
    global stop_coloumn_1
    global stop_coloumn_2
    global coloumn_0_0
    global coloumn_1_0
    global coloumn_2_0
    global coloumn_3_0
    global coloumn_4_0
    global coloumn_0_1
    global coloumn_1_1
    global coloumn_2_1
    global coloumn_3_1
    global coloumn_4_1
    global coloumn_0_2
    global coloumn_1_2
    global coloumn_2_2
    global coloumn_3_2
    global coloumn_4_2
    global spun
    global locked
    global spins

    #Call the randomize_odds function at the start of the spin
    if counter_spin <= 3:
        randomize_odds()

    #Empty the strings used for assigning text
    row_1_string = ""
    row_2_string = ""
    row_3_string = ""
    row_4_string = ""
    row_5_string = ""
    spun = True
    try: #Error handling incase .grid_remove isnt happy
        spin_button.grid_remove() #Remove spin button to prevent double clicks
    except:
        print("Remove error")
    old_0 = slot[0] #Move the rows down
    slot[0] = slot[4]
    old_1 = slot[1]
    slot[1] = old_0
    old_2 = slot[2]
    slot[2] = old_1
    old_3 = slot[3]
    slot[3] = old_2
    #old_4 = slot[4]
    slot[4] = old_3
    if counter_spin >= spins*0.3 and stop_coloumn_0 == False and locked == True: #Locking the first coloumn
        stop_coloumn_0 = True #Set the variable to stop the coloumn to true
        coloumn_0_0 = slot[0][0] #Save the current slot values to ensure it doesnt move
        coloumn_1_0 = slot[1][0]
        coloumn_2_0 = slot[2][0]
        coloumn_3_0 = slot[3][0]
        coloumn_4_0 = slot[4][0]
        row_1_string = f" {coloumn_0_0}" #Assign the saved values to the slot display
        row_2_string = f" {coloumn_1_0}"
        row_3_string = f">{coloumn_2_0}"
        row_4_string = f" {coloumn_3_0}"
        row_5_string = f" {coloumn_4_0}"
    elif stop_coloumn_0:
        row_1_string = f" {coloumn_0_0}" #Making sure the values are not overwritten
        row_2_string = f" {coloumn_1_0}"
        row_3_string = f">{coloumn_2_0}"
        row_4_string = f" {coloumn_3_0}"
        row_5_string = f" {coloumn_4_0}"
    else:
        row_1_string = f" {slot[0][0]}" #Normal spin case
        row_2_string = f" {slot[1][0]}"
        row_3_string = f">{slot[2][0]}"
        row_4_string = f" {slot[3][0]}"
        row_5_string = f" {slot[4][0]}"
    if counter_spin >= spins*0.5 and stop_coloumn_1 == False and locked == True: #Locking the second coloumn
        stop_coloumn_1 = True #Set the variable to stop the coloumn to true
        coloumn_0_1 = slot[0][1] #Save the current slot values to ensure it doesnt move
        coloumn_1_1 = slot[1][1]
        coloumn_2_1 = slot[2][1]
        coloumn_3_1 = slot[3][1]
        coloumn_4_1 = slot[4][1]
        row_1_string += f"{coloumn_0_1}" #Assign the saved values to the slot display
        row_2_string += f"{coloumn_1_1}"
        row_3_string += f"{coloumn_2_1}"
        row_4_string += f"{coloumn_3_1}"
        row_5_string += f"{coloumn_4_1}"
    elif stop_coloumn_1:
        row_1_string += f"{coloumn_0_1}" #Making sure the values are not overwritten
        row_2_string += f"{coloumn_1_1}"
        row_3_string += f"{coloumn_2_1}"
        row_4_string += f"{coloumn_3_1}"
        row_5_string += f"{coloumn_4_1}"
    else:
        row_1_string += f"{slot[0][1]}" #Normal spin case
        row_2_string += f"{slot[1][1]}"
        row_3_string += f"{slot[2][1]}"
        row_4_string += f"{slot[3][1]}"
        row_5_string += f"{slot[4][1]}"
    if counter_spin >= (spins *0.8) - 1 and stop_coloumn_2 == False and locked == True: #Locking the third coloumn
        stop_coloumn_2 = True #Set the variable to stop the coloumn to true
        coloumn_0_2 = slot[0][2] #Save the current slot values to ensure it doesnt move
        coloumn_1_2 = slot[1][2]
        coloumn_2_2 = slot[2][2]
        coloumn_3_2 = slot[3][2]
        coloumn_4_2 = slot[4][2]
        row_1_string += f"{coloumn_0_2} " #Assign the saved values to the slot display
        row_2_string += f"{coloumn_1_2} "
        row_3_string += f"{coloumn_2_2}<"
        row_4_string += f"{coloumn_3_2} "
        row_5_string += f"{coloumn_4_2} "
    elif stop_coloumn_2:
        row_1_string += f"{coloumn_0_2} " #Making sure the values are not overwritten
        row_2_string += f"{coloumn_1_2} "
        row_3_string += f"{coloumn_2_2}<"
        row_4_string += f"{coloumn_3_2} "
        row_5_string += f"{coloumn_4_2} "
    else:
        row_1_string += f"{slot[0][2]} " #Normal spin case
        row_2_string += f"{slot[1][2]} "
        row_3_string += f"{slot[2][2]}<"
        row_4_string += f"{slot[3][2]} "
        row_5_string += f"{slot[4][2]} "
    row_1_label.config(text=row_1_string) #Assign the created strings to the labels for display
    row_2_label.config(text=row_2_string)
    row_3_label.config(text=row_3_string)
    row_4_label.config(text=row_4_string)
    row_5_label.config(text=row_5_string)
    if counter_spin <= spins *0.8: # check if max spins is hit
        counter_spin += 1 #Iterate each time its spun
        #Debugging prints:
        #print(f"Locked: {locked}")
        #print(f"spins: {counter_spin}/{spins *0.8}")
        root.after(75,spin) #Rerun the function every 0.75 seconds
    else:
        stop_coloumn_0 = False #Reset bool values for locking coloumns
        stop_coloumn_1 = False
        stop_coloumn_2 = False
        spun = False #Reset if spun value
        counter_spin = 0 #Reset counter
        counter = 0 #Unneeded old method
        spin_button.grid(column=0,row=5) #Reassign spin button
        
#Assign labels
row_1_label = tk.Label(root, text= " | 👻|| 💲 || 💩| ", font=large_font)
row_2_label = tk.Label(root, text= " | 💲 || 🍒|| 💲 | ", font=large_font)
row_3_label = tk.Label(root, text= ">| 🏹|| 💩|| 🏹|<", font=large_font)
row_4_label = tk.Label(root, text= " | 🍒|| 🏹|| 👻| ", font=large_font)
row_5_label = tk.Label(root, text= " | 💩|| 👻|| 🍒| ", font=large_font)

#Assign spin button
spin_button = tk.Button(root, text="SPIN", command=spin,font=large_font)

#Place everyting on the widget
row_1_label.grid(column=0,row=0)
row_2_label.grid(column=0,row=1)
row_3_label.grid(column=0,row=2)
row_4_label.grid(column=0,row=3)
row_5_label.grid(column=0,row=4)
spin_button.grid(column=0,row=5)

#Run tk loop
root.mainloop()