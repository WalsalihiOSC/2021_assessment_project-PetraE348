##########################
#### OSC Computing #######
#### Author: Petra #######
####   Version: 5  #######
##########################

# Imports
from tkinter import *
from student_class import * 
import random

# Program
root = Tk()
root.config(bg="skyblue")
root.title("Ormiston Computing | Maths")
root.geometry("850x500")

'''Colours
# Blue - #25b1e9
# Pink - #FF00FF
# Purple - #9c57d5
# Green - #99dd1c
# Orange - #ffae00'''

# Define Class
class Interface:
    def __init__(self):
        self.notvalid = False
        self.main_frame()
    def main_frame(self):
        self.main=Frame(root, width="600", height="600",bg="skyblue")
        self.main.grid(column= 0, row= 0)
# Title
        title=Label(self.main, font=("Helvetica 18"), text="Ormiston Computing | Maths",bg="skyblue",)
        title.grid(column=2, row=1, pady= 50, sticky="NSEW")
# Student Name
        name_label=Label(self.main, text="Enter your name:", font=("Helvetica 16"), bg='#9c57d5',fg="white", borderwidth = 2, width = 20, relief="ridge")
        name_label.grid(column=1, row=3, padx=30,pady=20, sticky="NSEW")
        self.p_n=Entry(self.main,  font=("Helvetica 16"), borderwidth = 3, width = 15, relief="sunken")
        self.p_n.grid(column=2, row=3)
# Student Age
        age_label=Label(self.main, text="Enter your age: ",font=("Helvetica 16"), bg='#FF00FF',fg="white", borderwidth = 2, width = 20, relief="ridge")
        age_label.grid(column=1, row=4,padx=30, pady= 20,sticky="NSEW")
        self.p_a = Entry(self.main, font=("Helvetica 16"), borderwidth = 3, width = 15, relief="sunken")
        self.p_a.grid(column=2, row=4) 
# Difficulty Level
        level_label=Label(self.main, text="Select a level:",font=("Helvetica 16"), bg='#25b1e9',fg="white", borderwidth = 2, width = 20, relief="ridge")
        level_label.grid(column=1, row=5,padx=30, pady= 20,sticky="NSEW")          
# DROPDOWN MENU
        self.tkvar = StringVar(root)
        self.choices = ['One', 'Two', 'Three']
        self.tkvar.set('Select Level')
        self.dropdown = OptionMenu(self.main, self.tkvar, *self.choices)
        self.leveldropdown = self.dropdown.grid(column=2,row=5)
        def change_dropdown(*args):
            self.method = (self.tkvar.get())
        self.tkvar.trace('w', change_dropdown)
# Save Button
        self.submit = Button(self.main, text="  Submit ", font=("Helvetica 15"), bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.submit_check)
        self.submit.grid(column= 3, row=6 ,padx=20,sticky="NSEW")  
    
    def submit_check(self):
        
        self.player_n = (self.p_n.get().capitalize())
        self.player_a = self.p_a.get()
        self.player_l = self.tkvar.get()
        self.player = Student(self.player_n, self.player_a, self.player_l) 
        name_error = self.player.name_verification() 
        Label(self.main, text=name_error, fg='red', font=30, bg="skyblue").grid(column=3, row=3, sticky='w')
        age_error = self.player.age_verification()
        Label(self.main, text=age_error, fg='red', font=30, bg="skyblue").grid(column=3, row=4, sticky='w')
        level_error = self.player.level_verification()
        Label(self.main, text=level_error, fg='red', font=30, bg="skyblue").grid(column=3, row=5, sticky='w')
        if name_error == "✔ Valid                              " and age_error == "✔ Valid                              " and level_error == "✔ Valid                              ":
                   
            self.score_reset()
        else: 
            return "Invalid"

    def question_reload(self):
        if self.player_l == "One":
            self.num1update = random.randrange(1,20)
            self.num2update = random.randrange(1,20)
        elif self.player_l == "Two":
            self.num1update = random.randrange(1,50)
            self.num2update = random.randrange(1,50)
        else:
            self.num1update = random.randrange(1,100)
            self.num2update = random.randrange(1,100)

    def score_reset(self):
        self.count = 1
        self.score = 0
        self.questions_win()

    def questions_win(self):
        self.main.destroy()
        self.question_frame = Frame(root, width="600", height="600",bg="skyblue")
        self.question_frame.grid(row=0, column=0)
        count_label=Label(self.question_frame,font=("Helvetica 18"), text=f"Q:{self.count}", bg="skyblue")
        count_label.grid(column=1, row=1, pady= 50, padx=50, sticky="NSEW")
        title2_label=Label(self.question_frame, font=("Helvetica 18"), text=f"Ormiston Computing | Level {self.player_l}", bg="skyblue")
        title2_label.grid(column=2, row=1, pady= 50, padx=50, sticky="NSEW")
        self.question_reload()
        self.question = Label(self.question_frame,font=("Helvetica 35"), text=f" {self.num1update} + {self.num2update} =  ",bg="skyblue")
        self.question.grid(column=2, row=2, pady=20)
        score_label=Label(self.question_frame, text=f" {self.score} /10", font=("Helvetica 18"), bg="skyblue")
        score_label.grid(column=3, row=5)
        self.solving = Entry(self.question_frame, font=("Helvetica 30"), borderwidth = 5, width = 8, relief="sunken")
        self.solving.grid(column=2, row=3, pady=60)
        self.check = Button(self.question_frame,font=("Helvetica 15"), text=" Check", bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command= lambda: self.check_answer(self.solving))
        self.check.grid(column=3, row=4, padx=30)

    def correct_answer(self):                
        return self.num1update + self.num2update

    def check_answer(self,var1):
        
        if var1.get() == str(self.correct_answer()):
            self.score +=1  
            self.feed_back = Label(self.question_frame, text="✔ Correct!                                ",font=("Helvetica 10"), fg="green", bg="skyblue")
            self.feed_back.grid(column=3, row=3, sticky="W")
            self.check.grid_remove()
            self.question_win_nextb = Button(self.question_frame, text=" Next ",font=("Helvetica 15"), bg='#ffae00', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.nextbtn)
            self.question_win_nextb.grid(column=3,row=4,padx=30)
            self.count += 1
        elif len(var1.get())==0:
            Label(self.question_frame, text="✘ Must Enter An Answer", fg='red', font=("Helvetica 10"), bg="skyblue").grid(column=3, row=3, sticky='w')
        else:
            self.count +=1
            self.feed_back = Label(self.question_frame, text="✘ Wrong                               ", font=("Helvetica 15"), fg="red", bg="skyblue")
            self.feed_back.grid(column=3, row=3, sticky="W")
            self.check.grid_remove()
            self.question_win_nextb = Button(self.question_frame, text=" Next ",font=("Helvetica 15"), bg='#ffae00', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.nextbtn)
            self.question_win_nextb.grid(column=3,row=4,padx=30)
        if self.count == 11:
                        self.check.config(state=DISABLED)
                        self.check.unbind("<Button-1>")
                        self.time = 11
                        self.count=0
                        def countdown():
                                if self.time >= 0:
                                        # End of Q
                                        self.feed_back.grid_remove()
#BUTTON
                                        # Spawn 'finish' button
                                        Button(self.question_frame, text="Finish",font=50, bg='#25b1e9', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.end_stats).grid(column=3,row=4)
                                        # next Frame button
                                        self.time -= 1
                                else:   
                                        # Otherwise continue as normal
                                        global count
                                        self.check.config(state=NORMAL)
                        countdown()
    def nextbtn(self):
        self.question_frame.grid_forget()
        self.questions_win()
        self.solving.delete(0, 'end')

    def end_stats(self):
        self.question_frame.destroy()
        self.stats = Frame(root, width="600", height="600",bg="skyblue")
        self.stats.grid(row=0, column=0)
        #LABELS 
        #Title 'Maths Helper'
        Label(self.stats,  font=("Helvetica 18"),  text=f"Ormiston Computing | Stats",bg="skyblue").grid(column=2, row=1)
        #Label for player name
        Label(self.stats, text=f"Name:", font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=1, row=2, pady=20)
        Label(self.stats, text=f"Score:", font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=2, row=2, pady=20)
        Label(self.stats, text=f" {self.player_n}",font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=1, row=3)
        Label(self.stats, text=f" {self.score}/10",font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=2, row=3)
#BUTTONS
        self.restart = Button(self.stats, text="Restart", bg="#9c57d5",font=("Helvetica 15"), fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.restart_grid_destroy)
        self.restart.grid(column=3, row=4, pady=50)
        self.newplayer = Button(self.stats, text="New Player", bg="#FF00FF",font=("Helvetica 15"), fg="white", borderwidth = 2, width = 10, relief="ridge",  command=self.new_player_grid_destroy)
        self.newplayer.grid(column=1, row=4, pady=50)
#Creates the restart_grid_destroy function
# 1. Destroy stats grid
# 2. Calls the level_win function  
    def restart_grid_destroy(self):
                self.stats.destroy()
                self.score_reset()
#Creates the new_player_grid_destroy function
# 1. Destroys the stats grid
# 2. Calls the __init__ function
    def new_player_grid_destroy(self):
                self.stats.destroy()
                self.__init__()
Interface()
root.mainloop()

