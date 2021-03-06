from tkinter import *
root = Tk()

class interface:
#Class for welcome window
        def __init__(self):
            self.name_win = Frame(root, width="200", height="200")
            self.name_win.grid()

            #Title 'Student Details'
            self.title = Label(self.name_win, font=("Arial 18 bold underline"), text="MATHS HELPER").grid(column=3, row=0, pady=5)
            self.namel = Label(self.name_win, text="Enter your name: ", bg='#9c57d5').grid(column=3, row=1)
            self.name = Entry(self.name_win, text="            ")
            self.name.grid(column=4, row=1)
            self.submitb = Button(self.name_win, text="Submit", bg='#99dd1c', command=self.submit).grid(column=5, row=4)

        def submit(self):
            self.name = (self.name.get().title())
            self.name_win.grid_forget()
            self.level_win()

        def level_win(self):
            self.level_frame = Frame(root, width="200", height="200")
            self.level_frame.grid()
            self.title = Label(self.level_frame, text="MATHS HELPER").grid(column=3, row=0, pady=5)
            self.label = Label(self.level_frame, text="Select a level: ", fg='black').grid(column=3, row=1)
            self.level1 = Button(self.level_frame, text="Level 1", bg="#FF00FF", command=self.topic1_win ).grid(column=3, row=3)
            self.level2 = Button(self.level_frame, text="Level 2", bg="#99dd1c", command=self.topic2_win ).grid(column=3, row=4)
            self.level3 = Button(self.level_frame, text="Level 3", bg="#25b1e9", command=self.topic3_win ).grid(column=3, row=5)
            self.backlevel = Button(self.level_frame, text="Back", command=self.backlevel).grid(column=3, row=6)
        
        def backlevel(self):
            self.level_frame.grid_forget()
            self.__init__()
        
        def topic1_win(self):
            self.level_frame.grid_forget()
            self.topic1_frame = Frame(root, width="200", height="200")
            self.topic1_frame.grid()
            self.title = Label(self.topic1_frame, text="MATHS HELPER").grid(column=3, row=0, pady=5)
            self.label= Label(self.topic1_frame, text="Select a topic: ", fg='black').grid(column=3, row=1)
            self.addition1= Button(self.topic1_frame, text="Addition", bg="#FF00FF", command=self.questions1 ).grid(column=3, row=3)
            self.subtraction1 = Button(self.topic1_frame, text="Subtraction", bg="#99dd1c", command=self.questions1 ).grid(column=3, row=4)
            self.multiplication1 = Button(self.topic1_frame, text="Multiplication", bg="#25b1e9", command=self.questions1 ).grid(column=3, row=5)
            self.division1 = Button(self.topic1_frame, text="Division", bg="#25b1e9", command=self.questions1 ).grid(column=3, row=6)
            self.back = Button(self.topic1_frame, text="Back", command=self.back1).grid(column=3, row=8)
        
        def back1(self):
            self.topic1_frame.grid_forget()
            self.level_win()

        def topic2_win(self):
            self.level_frame.grid_forget()
            self.topic2_frame = Frame(root, width="200", height="200")
            self.topic2_frame.grid()
            self.title = Label(self.topic2_frame, text="MATHS HELPER").grid(column=3, row=0, pady=5)
            self.label= Label(self.topic2_frame, text="Select a topic: ", fg='black').grid(column=3, row=1)
            self.addition2= Button(self.topic2_frame, text="Addition", bg="#FF00FF", command=self.questions2  ).grid(column=3, row=3)
            self.subtraction2 = Button(self.topic2_frame, text="Subtraction", bg="#99dd1c", command=self.questions2  ).grid(column=3, row=4)
            self.multiplication2 = Button(self.topic2_frame, text="Multiplication", bg="#25b1e9", command=self.questions2  ).grid(column=3, row=5)
            self.division2 = Button(self.topic2_frame, text="Division", bg="#25b1e9", command=self.questions2 ).grid(column=3, row=6)
            self.back = Button(self.topic2_frame, text="Back", command=self.back2).grid(column=3, row=8)

        def back2(self):
            self.topic2_frame.grid_forget()
            self.level_win()

        def topic3_win(self):
            self.level_frame.grid_forget()
            self.topic3_frame = Frame(root, width="200", height="200")
            self.topic3_frame.grid()
            self.title = Label(self.topic3_frame, text="MATHS HELPER").grid(column=3, row=0, pady=5)
            self.label= Label(self.topic3_frame, text="Select a topic: ", fg='black').grid(column=3, row=1)
            self.addition3= Button(self.topic3_frame, text="Addition", bg="#FF00FF", command=self.questions3 ).grid(column=3, row=3)
            self.subtraction3 = Button(self.topic3_frame, text="Subtraction", bg="#99dd1c", command=self.questions3 ).grid(column=3, row=4)
            self.multiplication3 = Button(self.topic3_frame, text="Multiplication", bg="#25b1e9", command=self.questions3 ).grid(column=3, row=5)
            self.division3 = Button(self.topic3_frame, text="Division", bg="#25b1e9", command=self.questions3 ).grid(column=3, row=6)
            self.back = Button(self.topic3_frame, text="Back", command=self.back3).grid(column=3, row=8)
        
        def back3(self):
            self.topic3_frame.grid_forget()
            self.level_win()

        def questions1(self):
            self.topic1_frame.grid_forget()
            self.questions1_frame = Frame(root, width="200", height="200")
            self.questions1_frame.grid()
            self.title = Label(self.questions1_frame, text="Level One 'topic' ").grid(column=3, row=0, pady=5)
            self.back = Button(self.questions1_frame, text="Back", command=self.backq1).grid(column=3, row=4)
            self.finish = Button(self.questions1_frame, text="Finished", command=self.q1gridforget).grid(column=4, row=4)

        def backq1(self):
            self.questions1_frame.grid_forget()
            self.topic1_win()
            
#impliment loop?
        def questions2(self):
            self.topic2_frame.grid_forget()
            self.questions2_frame = Frame(root, width="200", height="200")
            self.questions2_frame.grid()
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
            self.questions3_frame.grid()
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
            self.leaderboard_frame.grid()
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
