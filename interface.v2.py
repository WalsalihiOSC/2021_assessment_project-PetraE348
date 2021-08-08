#Petra Edgar
#Maths Interface.20
#30/07/2021

#Imports
from tkinter import *
import random

#Window
root = Tk()
root.title("Maths Helper")
root.config(bg="skyblue")

#Hex Codes
#Purple #9c57d5
#Orange #ffae00
#Yellow #fff788
#Blue #25b1e9
#Green #99dd1c

num = [1,2,3,4,5,6,7,8,9,10]

#Defining class
class interface:

    def __init__(self):
        self.main_window = main_window

#Input Name Frame
    def welcome_frame(self):
        self.name_win = Frame(root, width="600", height="600",bg="skyblue")
        self.name_win.grid(row=0, column=0, padx=10, pady=5)
        self.title = Label(self.name_win, font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue",).grid(column=1, row=0, padx=150)
        self.player_name_label = Label(self.name_win, text="Enter your name: ", font=100, fg='#9c57d5',bg="skyblue").grid(column=1, row=1, pady=50)
        self.player_name.grid(column=1, row=2)
        self.submit_btn = Button(self.name_win, text="Submit",fg='black', font=50, bg='#99dd1c', command=self.checkinput).grid(column=1, row=4, pady=50)
#Name Entry 
        self.player_name = Entry(self.name_win, text="            ", font=50)

#Submit Name Entry & Test for Errors
    def check_input(self):
        # Get users input
        self.player_name = (self.player_name.get().capitalize())
    
        # If entry boxes are empty or year level is not between 1 and 6, error message is set
        if len(self.player_name)==0:
            Label(self.name_win, text="ERROR: Please enter your name")
        
        else:
            self.level_win()

#Level Selection Window       
    def level_win(self):
        self.level_frame = Frame(root, width="600", height="600",bg="skyblue")
        self.level_frame.grid(row=0, column=0, padx=10, pady=5)
        self.title = Label(self.level_frame, font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=1, row=0, padx=150)
        self.label = Label(self.level_frame, text=f"Hello {self.p_n}", font=50,bg="skyblue").grid(column=1, row=1, pady=5)
        self.label = Label(self.level_frame, text="Select a level: ", font=50, fg='black',bg="skyblue").grid(column=1, row=4)
        self.level1 = Button(self.level_frame, text="Level 1", font=50, bg="#FF00FF", command=self.topic1_win ).grid(column=1, row=5)
        self.level2 = Button(self.level_frame, text="Level 2", font=50, bg="#99dd1c", command=self.topic2_win ).grid(column=1, row=6)
        self.level3 = Button(self.level_frame, text="Level 3", font=50, bg="#25b1e9", command=self.topic3_win ).grid(column=1, row=7)
        self.backlevel = Button(self.level_frame, text="Back",bg='Orange', font=50, command=self.backlevel).grid(column=1, row=8)
    
    def backlevel(self):
                self.level_frame.destroy()
                self.welcome_frame()
    

    
    
    
    
    
    
    
    
    
    def checkb(self,var1):
        self.score =0
        if var1.get() == str(self.correct_answer()):
        self.correct = Label(self.questions1_frame, text="Correct!", fg="green")
        self.correct.grid(column=3, row=3)
        self.score +=1
        self.total_score = Label(self.questions1_frame, text=f"You have scored {self.score} /10!").grid(column=3, row=5)

        else:
            wrong = Label(self.questions1_frame, text="Wrong!", fg="red")
            wrong.grid(column=3, row=3)


interface()
root.title("Ormiston Computing- Maths Helper")
root.geometry("545x385")

root.mainloop()