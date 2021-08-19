#TO DO
# -Data Encapsulation
# -Make more aesthetically pleasing
# -Fix stats frame
####################################
####################################
##### Version: 4               #####
#####  Created By: Petra Edgar #####
#####  Date Created: 15/08/21  #####
####################################
####################################
#COLOUR CODES
#Purple #9c57d5
#Orange #ffae00
#Yellow #fff788
#Blue #25b1e9
#Green #99dd1c
#Pink #FF00FF

#imports tkinter (for labels, grids, buttons, frames)
from tkinter import *
#import random for random number generator
import random
#import tk font
#creates root for tkinter 
root = Tk()
root.config(bg="skyblue")
root.title("Ormiston Computing- Maths Helper")
root.geometry("600x400")

#Defines class as 'interface'
class interface:
#Creates the inital function
#__init__ function
#1. Creating menu frame
#2. Creating labels: dividers, title 'maths helper', 'enter your name', 'select a level'
#3. Creating drop down menu with levels 'one', 'two' & 'three'
#4. Creating button 'submit'
        def __init__(self):
                Grid.rowconfigure(root,0,weight=1)
                Grid.columnconfigure(root,0,weight=1)
 
                # Creating the menu frame
                self.menu = Frame(root, width="600", height="600",bg="skyblue")
                self.menu.grid(row=0, column=0)
                # These empty labels help with grid spacing
#LABELS
                # Title 'Maths Helper'
                Label(self.menu, font=("Helvetica 18"), text="MATHS HELPER",bg="skyblue",).grid(column=2, row=1, pady= 50, sticky="NSEW")
                # Label for player name
                Label(self.menu, text="Enter your name:", font=("Helvetica 13"), bg='#9c57d5',fg="white", borderwidth = 2, width = 20, relief="ridge").grid(column=1, row=3, padx=30,pady=20, sticky="NSEW")
                # Label for level selection 
                Label(self.menu, text="Select a level:",font=("Helvetica 13"), bg='#FF00FF',fg="white", borderwidth = 2, width = 20, relief="ridge").grid(column=1, row=4,padx=30, pady= 20,sticky="NSEW")
#ENTRY BOX
                # Entry for player_name/p_n
                self.p_n = Entry(self.menu, text="         ", font=50, borderwidth = 3, width = 15, relief="sunken")
                self.p_n.grid(column=2, row=3)
                #DROPDOWN MENU
                # Initiates dropdown menu for level selection
                self.tkvar = StringVar(root)
        
                # Sets options 'One', 'Two'& 'Three'
                self.choices = ['One', 'Two', 'Three']
                # Sets default selection to to 'Select Level'
                self.tkvar.set('Select Level')
                self.dropdown = OptionMenu(self.menu, self.tkvar, *self.choices)
                self.leveldropdown = self.dropdown.grid(column=2,row=4)
                # Allows user to change dropdown option
                def change_dropdown(*args):
                        self.method = (self.tkvar.get())
                self.tkvar.trace('w', change_dropdown)
#BUTTON         
                # Button for error checking 'submit_check'
                self.submit = Button(self.menu, text="  Submit ", font=("Helvetica 15"), bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.submit_check).grid(column= 3, row=5 ,padx=20,sticky="NSEW")

#Creates the submit_check function to validify player_name and level has been selected
#Note: I am allowing users to input integers as their name incase they want to try beat personal bests     
#submit_check function
#1. "Gets" the player_name and level variables (player_name is also capitalized for styling)
#2. If player_name has no letters then create the "Name required*" label
#3. Or if the level variable is "Select level" (default postion) then create the "Level Required*" label
#4. Otherwise go to the question_win function
        def submit_check(self):
                self.count = 1
                # Obtains player_name and level variables and captialises the first letter of player_name/p_n
                self.player_name = self.p_n.get().capitalize()
                self.level = self.tkvar.get()
                # If player_name/p_n entry box is empty then send error     
                if len(self.player_name)==0:
                        self.notvalid = True
                        Label(self.menu, text="Name Required*", fg='red', bg="skyblue").grid(column=3, row=3, sticky='w')     
                # If the level dropdown variable is still the default then send error
                elif self.level == "Select Level":
                        self.notvalid = True
                        Label(self.menu, text="Level Required*", fg='red', bg="skyblue").grid(column=3, row=4, sticky='w') 
                # Otherwise go to questions_win
                else:
                        self.notvalid = False
                        self.p_n.delete(0,'end')
                        self.question_win()

#############################################
############### QUESTION WINDOW #############
#############################################
#Creates the question_win function
#1. Sets the question counter variable (count) to 1
#2. Destroys the previous frames (menu) grid (Note: I do this because there is not a back button)
#3. Sets the players score to 0
#4. Creates question_frame
#5. Creates labels: dividers, 'maths helper'
#6. Calls question_reload function to create a label with a maths question
#7. Creates entry: solving
#9. Creates 'submit' button to error check inputted answer
        def question_win(self):
                # Question count = 1
                self.count = 1
                # Destrpy previous grid
                self.menu.destroy()
                # Player score = 0
                self.score = 0
                # Creates the question_frame
                self.question_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.question_frame.grid(row=0, column=0)
#LABELS
                # These empty labels help with grid spacing
                Label(self.question_frame, text="         ",bg="skyblue").grid(column=1, row=0, padx=40, pady=20)
                Label(self.question_frame, text="         ",bg="skyblue").grid(column=2, row=0, pady= 20)
                Label(self.question_frame, text="         ",bg="skyblue").grid(column=2, row=2, pady= 20)
                Label(self.question_frame, text="         ",bg="skyblue").grid(column=1, row=3, padx=40, pady=20)
                Label(self.question_frame, text="         ",bg="skyblue").grid(column=1, row=4, padx=40, pady=20)
                Label(self.question_frame, text="         ",bg="skyblue").grid(column=1, row=5, padx=40, pady=20)
                # Title 'Maths Helper'
                Label(self.question_frame, font=("Helvetica 18"), text=f"MATHS HELPER- Level {self.level}",bg="skyblue").grid(column=2, row=1)
#FUNCTION CALLED
                # Calls function to load questions
                self.question_reload()
#ENTRY
                # Entry box for answer
                self.solving = Entry(self.question_frame, text="      " ,font=50, borderwidth = 3, width = 15, relief="sunken")
                self.solving.grid(column=2, row=3)
#FUNCTION CALLED
                # Submit button which calls the error checking function )check_answer)
                self.check = Button(self.question_frame,font=("Helvetica 15"), text=" Check", bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command= lambda: self.check_answer(self.solving))
                self.check.grid(column=3, row=4)
#Creates the check_answer function
#1. If var1 is correct then add one point to the score, create label 'correct', remove the 'check' button, replace it with a next button and add one to the question count
#2. Otherwise create the 'wrong' label, remove the 'check'' button and replace it with the 'next' button and add one to question count
#3. If the question count (count) equals 11 then create the 'finish' button
        def check_answer(self,var1):
                # If var1 is correct then...
                if var1.get() == str(self.correct_answer()):
                        # Add 1 to score
                        self.score +=1
#LABEL
                        # Create 'Correct' label
                        self.feed_back = Label(self.question_frame, text="Correct!", fg="green", bg="skyblue")
                        self.feed_back.grid(column=3, row=3, sticky="W")
                        # Remove 'check' button
                        self.check.grid_remove()
#BUTTON
                        # Create the 'Next' button
                        self.question_win_nextb = Button(self.question_frame, text=" Next ",font=("Helvetica 15"), bg='#ffae00', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.nextbtn)
                        self.question_win_nextb.grid(column=3,row=4)
                        # Add 1 to count
                        self.count += 1
                #Otherwise
                else:
#LABEL
                        # Create 'wrong' label
                        self.feed_back = Label(self.question_frame, text="Wrong!", fg="red", bg="skyblue")
                        self.feed_back.grid(column=3, row=3, sticky="W")
                        # Remove 'check' button
                        self.check.grid_remove()
#BUTTON
                        # Create the 'Next' button
                        self.question_win_nextb = Button(self.question_frame, text=" Next ",font=("Helvetica 15"), bg='#ffae00', fg="white", borderwidth = 2, width = 10, relief="ridge", command=self.nextbtn)
                        self.question_win_nextb.grid(column=3,row=4)
                        # Add 1 to count
                        self.count += 1

                 # If the count == 11 times 
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
#Creates the nextbtn function
# 1. Removes question_win_nextb button 
# 2. Removes feedback labels
# 3. Calls question_reload function   
# 4. Clears entry box
# 5. Create submit button                   
        def nextbtn(self):
                self.question_win_nextb.grid_remove()
                self.feed_back.grid_remove()
                self.question_reload()
                self.solving.delete(0,'end')
#BUTTON
                self.check = Button(self.question_frame, font=("Helvetica 15"), text=" Check", bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command= lambda: self.check_answer(self.solving))
                self.check.grid(column=3, row=4)
#Creates the check_answer function
#Creates the question_reload function
# 1. If level variable is one then use range 1-20
# 2. If level variable is two then use range 1-50
# 3. If level variable is anything else then use range 1-100
# 4. Creates labels for questionn, score and count               
        def question_reload(self):
                if self.level == "One":
                        self.num1update = random.randrange(1,20)
                        self.num2update = random.randrange(1,20)
                elif self.level == "Two":
                        self.num1update = random.randrange(1,50)
                        self.num2update = random.randrange(1,50)
                else:
                        self.num1update = random.randrange(1,100)
                        self.num2update = random.randrange(1,100)
                self.question = Label(self.question_frame,font=50, text=f" {self.num1update} + {self.num2update} =  ",bg="skyblue").grid(column=2, row=2)
                Label(self.question_frame, text=f" {self.score} /10", font=50, bg="skyblue").grid(column=3, row=5)
                Label(self.question_frame, text=f"Q:{self.count}", font=50, bg="skyblue").grid(column=1, row=1)
#Creates the correct_answer function
# 1. Calculates the correct answer by adding the variables
        def correct_answer(self):                
                return self.num1update + self.num2update
                


#############################################
################## END STATS ################
#############################################

#Creates the end_stats function
# 1. Creates stats frame
# 2. 
        def end_stats(self):
                self.question_frame.destroy()
                self.stats = Frame(root, width="600", height="600",bg="skyblue")
                self.stats.grid(row=0, column=0)
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
                
        #font=("Helvetica 15"), text=" Check", bg='#99dd1c', fg="white", borderwidth = 2, width = 10, relief="ridge", command= lambda: self.check_answer(self.solving))
                #self.check.grid(column=3, row=4)
        
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
#End of 'interface' class
interface()
root.mainloop()


