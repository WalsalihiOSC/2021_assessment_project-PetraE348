from tkinter import *
root = Tk()
root.title("Maths Helper")
root.config(bg="skyblue")
import random
from PIL import ImageTk, Image
from tkinter import messagebox

num = [1,2,3,4,5,6,7,8,9,10]

class interface:
#Class for welcome window
        def __init__(self):
                self.name_win = Frame(root, width="600", height="600",bg="skyblue")
                self.name_win.grid(row=0, column=0, padx=10, pady=5)
                #Title 'Student Details'
                self.title = Label(self.name_win, font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue",).grid(column=1, row=0, padx=150)
                self.player_name_label = Label(self.name_win, text="Enter your name: ", font=50, fg='#9c57d5',bg="skyblue").grid(column=1, row=1, pady=50)
                self.player_name = Entry(self.name_win, text="            ", font=50)
                self.player_name.grid(column=1, row=2)
                self.submitb = Button(self.name_win, text="Submit",fg='black', font=50, bg='#99dd1c', command=self.submit).grid(column=1, row=4, pady=50)

        def submit(self):
                self.p_n = (self.player_name.get().capitalize())
                self.name_win.grid_forget()
                self.level_win()

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
                self.level_frame.grid_forget()
                self.__init__()
                
        def topic1_win(self):
                self.level_frame.grid_forget()
                self.topic1_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.topic1_frame.grid(row=0, column=0, padx=10, pady=5)
                self.title = Label(self.topic1_frame,font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=1, row=0, padx=150)
                self.label= Label(self.topic1_frame, text="Select a topic: ", font=50,bg="skyblue", fg='black').grid(column=1, row=1)
                self.addition1= Button(self.topic1_frame, text="Addition", font=50, bg="#FF00FF", command=self.questions1 ).grid(column=1, row=3)
                self.subtraction1 = Button(self.topic1_frame, text="Subtraction", font=50, bg="#99dd1c", command=self.questions1 ).grid(column=1, row=4)
                self.multiplication1 = Button(self.topic1_frame, text="Multiplication", font=50, bg="#25b1e9", command=self.questions1 ).grid(column=1, row=5)
                self.division1 = Button(self.topic1_frame, text="Division", font=50, bg="#9c57d5", command=self.questions1 ).grid(column=1, row=6)
                self.back = Button(self.topic1_frame, text="Back",bg='Orange', font=50, command=self.back1).grid(column=1, row=8)
                
        def back1(self):
                self.topic1_frame.grid_forget()
                self.level_win()

        def topic2_win(self):
                self.level_frame.grid_forget()
                self.topic2_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.topic2_frame.grid(row=0, column=0, padx=10, pady=5)
                self.title = Label(self.topic2_frame,font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=1, row=0, padx=150)
                self.label= Label(self.topic2_frame, text="Select a topic: ", font=50,bg="skyblue", fg='black').grid(column=1, row=1)
                self.addition2= Button(self.topic2_frame, text="Addition", font=50, bg="#FF00FF", command=self.questions2 ).grid(column=1, row=3)
                self.subtraction2 = Button(self.topic2_frame, text="Subtraction", font=50, bg="#99dd1c", command=self.questions2 ).grid(column=1, row=4)
                self.multiplication2 = Button(self.topic2_frame, text="Multiplication", font=50, bg="#25b1e9", command=self.questions2 ).grid(column=1, row=5)
                self.division2 = Button(self.topic2_frame, text="Division", font=50, bg="#9c57d5", command=self.questions2 ).grid(column=1, row=6)
                self.back = Button(self.topic2_frame, text="Back",bg='Orange', font=50, command=self.back2).grid(column=1, row=8)
        
        def back2(self):
                self.topic2_frame.grid_forget()
                self.level_win()

        def topic3_win(self):
                self.level_frame.grid_forget()
                self.topic3_frame = Frame(root, width="600", height="600",bg="skyblue")
                self.topic3_frame.grid(row=0, column=0, padx=10, pady=5)
                self.title = Label(self.topic3_frame,font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=1, row=0, padx=150)
                self.label= Label(self.topic3_frame, text="Select a topic: ", font=50,bg="skyblue", fg='black').grid(column=1, row=1)
                self.addition3= Button(self.topic3_frame, text="Addition", font=50, bg="#FF00FF", command=self.questions3 ).grid(column=1, row=3)
                self.subtraction3 = Button(self.topic3_frame, text="Subtraction", font=50, bg="#99dd1c", command=self.questions3 ).grid(column=1, row=4)
                self.multiplication3 = Button(self.topic3_frame, text="Multiplication", font=50, bg="#25b1e9", command=self.questions3 ).grid(column=1, row=5)
                self.division3 = Button(self.topic3_frame, text="Division", font=50, bg="#9c57d5", command=self.questions3 ).grid(column=1, row=6)
                self.back = Button(self.topic3_frame, text="Back",bg='Orange', font=50, command=self.back3).grid(column=1, row=8)
                
        def back3(self):
                self.topic3_frame.grid_forget()
                self.level_win()

        def questions1(self):
                self.topic1_frame.grid_forget()
                self.questions1_frame = Frame(root, width="600", height="600")
                self.questions1_frame.grid(row=0, column=0)
                self.title = Label(self.questions1_frame,font=("Arial 18 bold underline"), text="MATHS HELPER",bg="skyblue").grid(column=2, row=0, padx=150)
                self.title2 = Label(self.questions1_frame, text="Level One Addition ", font=50).grid(column=2, row=1)
                self.question_win()
                self.back = Button(self.questions1_frame, text="Back", command=self.backq1).grid(column=1, row=4)
                self.finish = Button(self.questions1_frame, text="Finished", command=self.q1gridforget).grid(column=3, row=0)
                self.solving = Entry(self.questions1_frame)
                self.solving.grid(column=3, row=3)

                self.check = Button(self.questions1_frame, text="Submit", command= lambda: self.checkb(self.solving))
                self.check.grid(column=3, row=4)

                self.nextb = Button(self.questions1_frame, text="Next", command=self.question_win)
                self.nextb.grid(column=3,row=2)
                
        def checkb(self,var1):
                if var1.get() == str(self.correct_answer()):
                        correct = Label(root, text="Correct!", fg="green")
                        correct.grid(column=1, row=1)
                        
                else:
                        wrong = Label(root, text="Wrong!", fg="red")
                        wrong.grid(column=1, row=1)

        def question_win(self):
                self.num1update = random.randrange(1,20)
                self.num2update = random.randrange(1,20)
                
                question = Label(self.questions1_frame, text=f"{self.num1update} + {self.num2update} = ")
                question.grid(column=2, row=2)

        def correct_answer(self):                
                return self.num1update + self.num2update


        def backq1(self):
                self.questions1_frame.grid_forget()
                self.topic1_win()
                
        #impliment loop?
        def questions2(self):
                self.topic2_frame.grid_forget()
                self.questions2_frame = Frame(root, width="600", height="600")
                self.questions2_frame.grid(row=0, column=0, padx=10, pady=5)
                self.title = Label(self.questions2_frame, text="Level Two 'topic' ").grid(column=3, row=0, pady=5)
                self.back = Button(self.questions2_frame, text="Back", command=self.backq2).grid(column=3, row=4)
                self.finish = Button(self.questions2_frame, text="Finished", command=self.q2gridforget).grid(column=4, row=4)

        def backq2(self):
                self.questions2_frame.grid_forget()
                self.topic2_win()
                

        #impliment loop?
        def questions3(self):
                self.topic3_frame.grid_forget()
                self.questions3_frame = Frame(root, width="200", height="200")
                self.questions3_frame.grid(row=0, column=0, padx=10, pady=5)
                self.title = Label(self.questions3_frame, text="Level Three 'topic' ").grid(column=3, row=0, pady=5)
                self.back = Button(self.questions3_frame, text="Back", command=self.backq3).grid(column=3, row=4)
                self.finish = Button(self.questions3_frame, text="Finished", command=self.q3gridforget).grid(column=4, row=4)

        def backq3(self):
                self.questions3_frame.grid_forget()
                self.topic3_win()
        #impliment loop?
        def q1gridforget(self):
                self.questions1_frame.grid_forget()
                self.leaderboard()
        def q2gridforget(self):
                self.questions2_frame.grid_forget()
                self.leaderboard()
        def q3gridforget(self):
                self.questions3_frame.grid_forget()
                self.leaderboard()
        
        
        def leaderboard(self):
                self.leaderboard_frame = Frame(root, width="200", height="200")
                self.leaderboard_frame.grid(row=0, column=0, padx=10, pady=5)
                self.title = Label(self.leaderboard_frame, text="MATHS HELPER").grid(column=3, row=0, pady=5)
                self.label = Label(self.leaderboard_frame, text="leaderboard").grid(column=3, row=1, pady=5)
                self.restart = Button(self.leaderboard_frame, text="Restart", command=self.restartgridforget).grid(column=2, row=2, pady=5)
                self.newplayer = Button(self.leaderboard_frame, text="New Player", command=self.npgridforget).grid(column=3, row=2, pady=5)
                
        def restartgridforget(self):
                self.leaderboard_frame.grid_forget()
                self.level_win()

        def npgridforget(self):
                self.leaderboard_frame.grid_forget()
                self.__init__()

interface()

root.title("Ormiston Course Selection")
root.geometry("545x385")

root.mainloop()

