

class Student:
    
    def __init__(self, player_n, player_l, player_a):
        self.player_name = player_n
        self.player_lvl = player_l
        self.player_age = player_a
        
    def main_checking(self):
        if len(self.player_name)==0:
            self.notvalid = True
            self.p_n_fail()
        elif self.player_age==0:
            self.notvalid = True
            self.p_a_empty()
        elif self.player_age >11:
            self.notvalid = True
            self.p_a_fail()
        elif self.player_age <5:
            self.p_a_fail()
        elif self.player_lvl == "Select Level":
            self.notvalid = True
            self.p_lvl_fail()
        else:
            self.notvalid = False
            self.check_pass()
    def question_reload(self):
        if self.level == "One":
            self.level_one_range()
        elif self.level == "Two":
            self.level_two_range()
        else:
            self.level_three_range()

    def check_answer(self,var1, count):
        if len(var1.get())==0:
            self.feedback_empty()
        else:
            if var1.get() == str(self.correct_answer()):
                self.score +=1
                self.feedback_correct()
                self.check.grid_remove()
                self.next_button_create()
            else:
                self.feedback_wrong()
                self.check.grid_remove()
                self.next_button_create()
                 
                 # If the count == 11 times 
                
            
    def write_file(self):
        results_file = open("math_results.text", "a")
        results_file.write("-------------------------\n")
        results_file.write(f"Student Name: {self.student_name} \n"
                            f"Year Level: {self.range} \n"
                            f"Operation: {self.difficulty}\n")
        
        results_file.write("-------------------------\n")
        results_file.close()
        
    
        
        