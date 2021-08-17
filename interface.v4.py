from tkinter import *
root = Tk()
root.title("Maths Helper")
root.config(bg="skyblue")
import random

#Define class
class interface:
#Class for welcome window
        def __init__(self):
                #Creating the menu frame
                #Creating the menu frame
                self.menu = Frame(root, width="600", height="600",bg="skyblue")
                self.menu.grid(row=0, column=0)
                #Title 'Maths Helper'
                Label(self.menu, text="         ",bg="skyblue").grid(column=1, row=1)
                Label(self.menu, text="         ",bg="skyblue").grid(column=2, row=0, pady= 20)
                Label(self.menu, text="         ",bg="skyblue").grid(column=2, row=2, pady= 20)
                Label(self.menu, font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue",).grid(column=2, row=1)
                #Label for player name
                Label(self.menu, text="Enter your \nname:", font=100, fg='#9c57d5',bg="skyblue").grid(column=1, row=3, padx=30)
                #Entry for player name
                self.p_n = Entry(self.menu, text="         ", font=50)
                self.p_n.grid(column=2, row=3)
                #Lable for level selection 
                Label(self.menu, text="Select a \nlevel:", font=50, fg='black',bg="skyblue").grid(column=1, row=4)
                Button(self.menu, text="done", command=self.done).grid(column=3, row=5)
                #Dropdown menu for levels
                self.tkvar = StringVar(root)
        
        # Set options
                self.choices = ['One', 'Two', 'Three']
                self.tkvar.set('Select Level')
                self.dropdown = OptionMenu(self.menu, self.tkvar, *self.choices)
        
        # Create Label
                self.leveldropdown = self.dropdown.grid(column=2,row=4)
        
                def change_dropdown(*args):
                        self.method = (self.tkvar.get())
                self.tkvar.trace('w', change_dropdown)
                self.submit = Button(self.menu, text="  Submit ", font=50, bg='#99dd1c', command=self.submit_check).grid(column= 3, row=4 ,padx=20)
        
        #defining function (submit) which error checks name
        def submit_check(self):
                self.count = 1
                #captialises the first letter of players name
                self.player_name = self.p_n.get().capitalize()
                self.level = self.tkvar.get()
                #if player name entry box is empty then sent error otherwise continue to questions frame & destroy current frame        
                if len(self.player_name)==0:
                        self.notvalid = True
                        Label(self.menu, text="Name Required*", fg='red').grid(column=3, row=1, sticky='e')     
                
                elif self.level == "Select Level":
                        self.notvalid = True
                        Label(self.menu, text="Level Required*", fg='red').grid(column=3, row=2, sticky='e') 
                else:
                        self.notvalid = False
                        self.questions_win1()

#############################################
############### LEVEL WINDOWS ###############
#############################################

#####################
##### LEVEL ONE #####
#####################
        #defines question win function
        def questions_win1(self):
                self.count = 1
                self.menu.grid_remove()
                self.score = 0
                #creates the question1 frame
                self.questions1_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.questions1_frame.grid(row=0, column=0)
                Label(self.questions1_frame, text="         ",bg="skyblue").grid(column=1, row=0, padx=40, pady=20)
                Label(self.questions1_frame, text="         ",bg="skyblue").grid(column=2, row=0, pady= 20)
                Label(self.questions1_frame, text="         ",bg="skyblue").grid(column=2, row=2, pady= 20)
        
                #title "Maths Helper"
                Label(self.questions1_frame,font=("Arial 18 bold underline"), text=f"MATHS HELPER- Level {self.level}",bg="skyblue").grid(column=2, row=1)

                #calls function for questions
                self.question_reload1()
                #entry for answer
                self.solving = Entry(self.questions1_frame, text="      " ,font=50)
                self.solving.grid(column=2, row=3)
                
                self.submit_spawn()
                #submit button
                self.check = Button(self.questions1_frame, text="Submit", font=50, bg='#99dd1c', command= lambda: self.checkb1(self.solving))
                self.check.grid(column=3, row=4)

        def submit_spawn(self):
                Label(self.questions1_frame, text="         ",bg="skyblue").grid(column=1, row=3, padx=40, pady=20)
                Label(self.questions1_frame, text="         ",bg="skyblue").grid(column=1, row=4, padx=40, pady=20)
                Label(self.questions1_frame, text="         ",bg="skyblue").grid(column=1, row=5, padx=40, pady=20)
                
                #next button for new question

        def checkb1(self,var1):

                
                if var1.get() == str(self.correct_answer()):
                        self.score +=1
                        self.feed_back = Label(self.questions1_frame, text="Correct!", fg="green")
                        self.feed_back.grid(column=3, row=3)
                        self.solving.delete(0,'end')
                        self.check.grid_remove()
                        self.questions1_nextb = Button(self.questions1_frame, text=" Next ",font=50, bg='#99dd1c', command=self.nextbtn)
                        self.questions1_nextb.grid(column=3,row=4)
                        self.count += 1

                else:
                        self.feed_back = Label(self.questions1_frame, text="Wrong!", fg="red")
                        self.feed_back.grid(column=3, row=3)
                        self.solving.delete(0,'end')
                        self.check.grid_remove()
                        self.questions1_nextb = Button(self.questions1_frame, text=" Next ",font=50, bg='#99dd1c', command=self.nextbtn)
                        self.questions1_nextb.grid(column=3,row=4)
                        self.count += 1

                 # button == 10 times 
                if self.count == 11:
                        self.check.config(state=DISABLED)
                        self.check.unbind("<Button-1>")
                        self.time = 11
                        self.count=0
                        def countdown():
                                if self.time >= 0:
                                        # End of Q
                                        self.feed_back.grid_remove()
                                        Button(self.questions1_frame, text=" End game  ",font=50, bg='#99dd1c', command=self.leaderboard).grid(column=3,row=4)
                                        # next Frame button
                                        self.time -= 1
                                else:
                                        global count
                                        self.check.config(state=NORMAL)
                        countdown()
                        
                        
        def nextbtn(self):
                self.questions1_nextb.grid_remove()
                self.feed_back.grid_remove()
                self.question_reload1()
                self.check = Button(self.questions1_frame, text="Submit", font=50, bg='#99dd1c', command= lambda: self.checkb1(self.solving))
                self.check.grid(column=3, row=4)
                
        def question_reload1(self):

                if self.level == "One":
                        self.num1update = random.randrange(1,20)
                        self.num2update = random.randrange(1,20)

                elif self.level == "Two":
                        self.num1update = random.randrange(1,50)
                        self.num2update = random.randrange(1,50)
                
                else:
                        self.num1update = random.randrange(1,100)
                        self.num2update = random.randrange(1,100)
                        
                
                self.question = Label(self.questions1_frame,font=50, text=f" {self.num1update} + {self.num2update} =  ",bg="skyblue").grid(column=2, row=2)
                Label(self.questions1_frame, text=f" {self.score} /10", font=50, bg="skyblue").grid(column=3, row=5)
                Label(self.questions1_frame, text=f"Q:{self.count}", font=50, bg="skyblue").grid(column=1, row=1)

        def correct_answer(self):                
                return self.num1update + self.num2update
                
                
        def q1gridforget(self):
                self.questions1_frame.destroy()
                self.leaderboard()

#######################        
##### LEADERBOARD #####     
#######################
        def done(self):
                self.menu.destroy()
                self.checkb1.destroy()
                self.submit_spawn.destroy()
                self.leaderboard()

        def leaderboard(self):
                #self.questions1_frame.grid_remove()
                self.leaderboard_frame = Frame(root, width="200", height="200")
                self.leaderboard_frame.grid(row=0, column=0, padx=10, pady=5)
                self.restart = Button(self.leaderboard_frame, text="Restart", command=self.restartgridforget).grid(column=3, row=5, pady=5)
                self.newplayer = Button(self.leaderboard_frame, text="New Player", command=self.npgridforget).grid(column=1, row=5, pady=5)
                
                self.leaderboard_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.leaderboard_frame.grid(row=0, column=0)
                #Title 'Maths Helper'
                Label(self.leaderboard_frame, text="         ",bg="skyblue").grid(column=1, row=1)
                Label(self.leaderboard_frame, text="         ",bg="skyblue").grid(column=2, row=0, pady= 20)
                Label(self.leaderboard_frame, text="         ",bg="skyblue").grid(column=2, row=2, pady= 20)
                #Label for player name
                Label(self.leaderboard_frame, text=f"Name: {self.player_name}           Score: {self.score}/10", font=100, fg='#9c57d5',bg="skyblue").grid(column=1, row=3)
        
                
        def restartgridforget(self):
                self.leaderboard_frame.destroy()
                self.level_win()

        def npgridforget(self):
                self.leaderboard_frame.destroy()
                self.__init__()

interface()

root.title("Ormiston Computing- Maths Helper")
root.geometry("600x400")

root.mainloop()