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
root.geometry("600x400")

'''Colours
# Blue - #25b1e9
# Pink - #FF00FF
# Purple - #9c57d5
# Green - #99dd1c
# Orange - #ffae00'''

# Define Class
class Interface:
    #Initial Function
    #__init__ function
    #1. Creating menu frame
    #2. Creating title 'maths helper', 'enter your name', 'enter your age', 'select a level'
    #3. Creating drop down menu with levels 'one', 'two' & 'three'
    #4. Creating button 'submit'
    def __init__(self):
        #Set variable for error checking
        self.notvalid = False
        self.main_frame()
    # Main Frame- Player_name, Player_age, Player_level
    def main_frame(self):
        self.main = Frame(root, width="600", height="600",bg="skyblue")
        self.main.grid(column= 0, row= 0)
    
        # Title
        Label(self.main, font=("Helvetica 18"), text="Ormiston Computing | Maths",bg="skyblue",).grid(column=2, row=1, pady= 50, sticky="NSEW")

        # Student Name
        Label(self.main, text="Enter your name:", font=("Helvetica 13"), bg='#9c57d5',fg="white", borderwidth = 2, width = 20, relief="ridge").grid(column=1, row=3, padx=30,pady=20, sticky="NSEW")
        self.p_n=Entry(self.main, text="         ", font=50, borderwidth = 3, width = 15, relief="sunken")
        self.p_n.grid(column=2, row=3)
        
        # Student Age
        Label(self.main, text="Enter your age: ",font=("Helvetica 13"), bg='#FF00FF',fg="white", borderwidth = 2, width = 20, relief="ridge").grid(column=1, row=4,padx=30, pady= 20,sticky="NSEW")
        self.p_a = Entry(self.main, text="         ", font=50, borderwidth = 3, width = 15, relief="sunken")
        self.p_a.grid(column=2, row=4)
        
        # Difficulty Level
        Label(self.main, text="Select a level:",font=("Helvetica 13"), bg='#25b1e9',fg="white", borderwidth = 2, width = 20, relief="ridge").grid(column=1, row=5,padx=30, pady= 20,sticky="NSEW")     
       
        # DROPDOWN MENU
        # Initiates dropdown menu for level selection
        self.tkvar = StringVar(root)
        # Set options
        self.choices = ['One', 'Two', 'Three']
        # Sets default selection to to 'Select Level'
        self.tkvar.set('Select Level')
        self.dropdown = OptionMenu(self.main, self.tkvar, *self.choices)
        self.leveldropdown = self.dropdown.grid(column=2,row=5)
        # Allows user to change dropdown option
        def change_dropdown(*args):
            self.method = (self.tkvar.get())
        self.tkvar.trace('w', change_dropdown)
        # Save Button
        self.submit = Button(self.main, text="  Submit ", font=("Helvetica 15"), bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.submit_check).grid(column= 3, row=5 ,padx=20,sticky="NSEW")  
    def submit_check(self):
         # Obtains player_name, player_age and level variables and captialises the first letter of player_n/p_n
        self.player_n = (self.p_n.get().capitalize())
        self.player_a = self.p_a.get()
        self.player_l = self.tkvar.get()
        
        # Creating instance of students class with users input
        self.player = Student(self.player_n, self.player_a, self.player_l) 
        self.player.main_checking()

    

    def p_n_fail(self):
        Label(self.menu, text="Name Required*", fg='red', bg="skyblue").grid(column=3, row=3, sticky='w')
    def p_a_empty(self):
        Label(self.menu, text="Age Required*", fg='red', bg="skyblue").grid(column=3, row=4, sticky='w')
    def p_a_fail(self):
        Label(self.menu, text="Must be 5-11*", fg='red', bg="skyblue").grid(column=3, row=4, sticky='w')
    def p_lvl_fail(self):
        Label(self.menu, text="Level Required*", fg='red', bg="skyblue").grid(column=3, row=5, sticky='w') 
    
        # If entry boxes are empty or year level is not between 1 and 6, error message is set
    def check_pass(self):
        self.questions_win()  
    def level_one_range(self):
        self.num1update = random.randrange(1,20)
        self.num2update = random.randrange(1,20)
    def level_two_range(self):
        self.num1update = random.randrange(1,50)
        self.num2update = random.randrange(1,50)
    def level_three_range(self):
        self.num1update = random.randrange(1,100)
        self.num2update = random.randrange(1,100)

    
    def questions_win(self):
# Question count = 1
        self.count = 1
        # Destrpy previous grid
        self.main.destroy()
        # Player score = 0
        self.score = 0
        # Creates the question_frame
        self.question_frame = Frame(root, width="600", height="600",bg="skyblue")
        self.question_frame.grid(row=0, column=0)
        # New widgets (labels, entry boxes and buttons)
        # Title
        Label(self.question_frame, font=("Helvetica 18"), text=f"MATHS HELPER- Level {self.l}", bg="skyblue").grid(column=2, row=1)
        
        self.question_reload()
        self.question = Label(self.question_frame,font=50, text=f" {self.num1update} + {self.num2update} =  ",bg="skyblue").grid(column=2, row=2)
        Label(self.question_frame, text=f" {self.score} /10", font=50, bg="skyblue").grid(column=3, row=5)
        Label(self.question_frame, text=f"Q:{self.count}", font=50, bg="skyblue").grid(column=1, row=1)
#ENTRY
        # Entry box for answer
        self.solving = Entry(self.question_frame, text="      " ,font=50, borderwidth = 3, width = 15, relief="sunken")
        self.solving.grid(column=2, row=3)
#FUNCTION CALLED
                # Submit button which calls the error checking function )check_answer)
        self.check = Button(self.question_frame,font=("Helvetica 15"), text=" Check", bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command= lambda: self.check_answer(self.solving))
        self.check.grid(column=3, row=4)
    def feedback_empty(self):
        self.empty_entry =  Label(self.question_frame,font=("Helvetica 18"), text="Must be filled*", fg="red", bg="skyblue")
        self.feed_back.grid(column=3, row=3, sticky="W")
    def feedback_correct(self):
        self.feed_back = Label(self.question_frame,font=("Helvetica 18"), text="Correct!", fg="green", bg="skyblue")
        self.feed_back.grid(column=3, row=3, sticky="W")
    def next_button_create(self):
        self.question_win_nextb = Button(self.question_frame, text=" Next ",font=("Helvetica 15"), bg='#FF00FF', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.nextbtn)
        self.question_win_nextb.grid(column=3,row=4)  
        self.count += 1
    
    def feedback_wrong(self):
        self.feed_back = Label(self.question_frame,font=("Helvetica 18"), text="Wrong!", fg="red", bg="skyblue")
        self.feed_back.grid(column=3, row=3, sticky="W")
    def count_checker(self):
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
                    Button(self.question_frame,font=("Helvetica 15"), text=" Finish ", bg='#25b1e9', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.end_stats).grid(column=3,row=4)
                    # next Frame button
                    self.time -= 1
                else:   
                    # Otherwise continue as normal
                    self.count
                    self.check.config(state=NORMAL)
            countdown()
    def correct_answer(self):                
                return self.num1update + self.num2update
                
    
    def end_stats(self):
        
        #LABELS 
        #Title 'Maths Helper'
                Label(self.stats,  font=("Helvetica 18"),  text=f"MATHS HELPER- Level {self.level}",bg="skyblue").grid(column=2, row=1)
                #Label for player name
                Label(self.stats, text=f"Name:", font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=1, row=2, pady=20)
                Label(self.stats, text=f"Score:", font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=2, row=2, pady=20)
                Label(self.stats, text=f" {self.player_name}",font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=1, row=3)
                Label(self.stats, text=f" {self.score}/10",font=("Helvetica 18"), fg='black',bg="skyblue").grid(column=2, row=3)
#BUTTONS
                self.restart = Button(self.stats, text="Restart", bg="#9c57d5",font=("Helvetica 15"), fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.restart_grid_destroy).grid(column=3, row=4, pady=50)
                self.newplayer = Button(self.stats, text="New Player", bg="#FF00FF",font=("Helvetica 15"), fg="white", borderwidth = 2, width = 10, relief="ridge",  command=self.new_player_grid_destroy).grid(column=1, row=4, pady=50)
#Creates the restart_grid_destroy function
# 1. Destroy stats grid
# 2. Calls the level_win function  
    def restart_grid_destroy(self):
                self.stats.destroy()
                self.question_win()
#Creates the new_player_grid_destroy function
# 1. Destroys the stats grid
# 2. Calls the __init__ function
    def new_player_grid_destroy(self):
                self.stats.destroy()
                self.__init__()
Interface()
root.mainloop()

