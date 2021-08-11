from tkinter import *
root = Tk()
root.title("Maths Helper")
root.config(bg="skyblue")
import random


num = [1,2,3,4,5,6,7,8,9,10]

class interface:
#Class for welcome window
        def __init__(self):
                self.name_win = Frame(root, width="600", height="600",bg="skyblue")
                self.name_win.grid(row=0, column=0)
                #Title 'Student Details'
                self.title = Label(self.name_win, font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue",).grid(column=1, row=0)
                self.player_name_label = Label(self.name_win, text="Enter your name: ", font=100, fg='#9c57d5',bg="skyblue").grid(column=1, row=1)
                self.player_name = Entry(self.name_win, text="            ", font=50)
                self.player_name.grid(column=1, row=2)
                self.label = Label(self.name_win, text="Select a level: ", font=50, fg='black',bg="skyblue").grid(column=2, row=1)
                self.level1 = Button(self.name_win, text="Level 1", font=50, bg="#FF00FF", command=self.submit1 ).grid(column=2, row=2)
                self.level2 = Button(self.name_win, text="Level 2", font=50, bg="#99dd1c", command=self.submit2 ).grid(column=2, row=3)
                self.level3 = Button(self.name_win, text="Level 3", font=50, bg="#25b1e9", command=self.submit3 ).grid(column=2, row=4)
                self.exit = Button(self.name_win, text="Exit",bg='Orange', font=50, command=self.quit).grid(column=2, row=5)
        
        def submit1(self):
                self.count = 1
                self.p_n = self.player_name.get().capitalize()
                if len(self.p_n) == 0:
                        self.notvalid = True
                        Label(self.name_win, text="Name Required*", fg='red').grid(column=1, row=2, sticky='e') 
                else:
                        self.name_win.destroy()
                        self.questions1()
                
        def submit2(self):
                self.count = 1
                self.p_n = self.player_name.get().capitalize()
                if len(self.p_n) == 0:
                        self.notvalid = True
                        Label(self.name_win, text=" Error: Name Required!").grid(column=1, row=2, pady=50) 
                else:
                        self.name_win.destroy()
                        self.questions2()

        def submit3(self):
                self.count = 1
                self.p_n = self.player_name.get().capitalize()
                if len(self.p_n) == 0:
                        self.notvalid = True
                        Label(self.name_win, text=" Error: Name Required!").grid(column=1, row=2, pady=50) 
                else:
                        self.name_win.destroy()
                        self.questions3()


                
        
        def quit(self):
            self.name_win.destroy()   
        
        def questions1(self):
                self.name_win.destroy()
                self.questions1_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.questions1_frame.grid(row=0, column=0)
                self.title = Label(self.questions1_frame,font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=2, row=0)
                self.title2 = Label(self.questions1_frame, text="Level One", font=50,bg="skyblue").grid(column=2, row=1)
                self.question_win()
                self.back = Button(self.questions1_frame, text="Back",bg='Orange', font=50, command=self.backq).grid(column=1, row=4, padx=40, pady=50)
                self.finish = Button(self.questions1_frame, text="Finished", font=50, bg="#9c57d5",command=self.q1gridforget).grid(column=3, row=0)
                self.solving = Entry(self.questions1_frame, text="      " ,font=50)
                self.solving.grid(column=3, row=3)
                self.check = Button(self.questions1_frame, text="Submit", font=50, bg='#99dd1c', command= lambda: self.checkb(self.solving))
                self.check.grid(column=3, row=4)
                self.nextb = Button(self.questions1_frame, text="Next", command=self.question_win)
                self.nextb.grid(column=3,row=2) 

        def questions2(self):
                self.name_win.destroy()
                self.questions2_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.questions2_frame.grid(row=0, column=0)
                self.title = Label(self.questions2_frame,font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=2, row=0)
                self.title2 = Label(self.questions2_frame, text="Level Two", font=50,bg="skyblue").grid(column=2, row=1)
                self.question_win()
                self.back = Button(self.questions2_frame, text="Back",bg='Orange', font=50, command=self.backq).grid(column=1, row=4, padx=40, pady=50)
                self.finish = Button(self.questions2_frame, text="Finished", font=50, bg="#9c57d5",command=self.q1gridforget).grid(column=3, row=0)
                self.solving = Entry(self.questions2_frame, text="      " ,font=50)
                self.solving.grid(column=3, row=3)
                self.check = Button(self.questions2_frame, text="Submit", font=50, bg='#99dd1c', command= lambda: self.checkb(self.solving))
                self.check.grid(column=3, row=4)
                self.nextb = Button(self.questions2_frame, text="Next", command=self.question_win)
                self.nextb.grid(column=3,row=2) 
        
        def questions3(self):
                self.name_win.destroy()
                self.questions3_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.questions3_frame.grid(row=0, column=0)
                self.title = Label(self.questions3_frame,font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=2, row=0)
                self.title2 = Label(self.questions3_frame, text="Level Three", font=50,bg="skyblue").grid(column=2, row=1)
                self.question_win()
                self.back = Button(self.questions3_frame, text="Back",bg='Orange', font=50, command=self.backq).grid(column=1, row=4, padx=40, pady=50)
                self.finish = Button(self.questions3_frame, text="Finished", font=50, bg="#9c57d5",command=self.q3gridforget).grid(column=3, row=0)
                self.solving = Entry(self.questions3_frame, text="      " ,font=50)
                self.solving.grid(column=3, row=3)
                self.check = Button(self.questions3_frame, text="Submit", font=50, bg='#99dd1c', command= lambda: self.checkb(self.solving))
                self.check.grid(column=3, row=4)
                self.nextb = Button(self.questions3_frame, text="Next", command=self.question_win)
                self.nextb.grid(column=3,row=2) 
        
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
                
                

        def question_win(self):
                self.num1update = random.randrange(1,20)
                self.num2update = random.randrange(1,20)
                
                question = Label(self.questions1_frame,font=50, text=f"{self.num1update} + {self.num2update} = ",bg="skyblue")
                question.grid(column=2, row=2,pady=20)
                

        def correct_answer(self):                
                return self.num1update + self.num2update


        def backq(self):
                self.questions1_frame.destroy()
                self.__init__()
                self.player_name.delete(0,'end')
                
                
        def q1gridforget(self):
                self.questions1_frame.destroy()
                self.leaderboard()
        def q2gridforget(self):
                self.questions2_frame.destroy()
                self.leaderboard()
        def q3gridforget(self):
                self.questions3_frame.destroy()
                self.leaderboard()
        
        
        def leaderboard(self):
                self.leaderboard_frame = Frame(root, width="200", height="200")
                self.leaderboard_frame.grid(row=0, column=0, padx=10, pady=5)
                self.title = Label(self.leaderboard_frame, text="MATHS HELPER").grid(column=3, row=0, pady=5)
                self.label = Label(self.leaderboard_frame, text="leaderboard").grid(column=3, row=1, pady=5)
                self.restart = Button(self.leaderboard_frame, text="Restart", command=self.restartgridforget).grid(column=2, row=2, pady=5)
                self.newplayer = Button(self.leaderboard_frame, text="New Player", command=self.npgridforget).grid(column=3, row=2, pady=5)
                
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

