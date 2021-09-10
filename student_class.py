class Student:
    
    def __init__(self, player_n, player_a, player_l):
        self.player_name = player_n
        self.player_age = player_a
        self.player_lvl = player_l
        
    def name_verification(self):
        if len(self.player_name)==0:
            self.notvalid = True
            return "✘ Must Enter A Name"
        else:
            self.notvalid = False 
            return "✔ Valid                              "

    def age_verification(self):
        try: 
            responce = int(self.player_age)
            
            if responce   in [5,6,7,8,9,10,11]:
                self.notvalid = True
                return "✔ Valid                              "
            else:
                self.notvalid = False 
                return "✘ Must Be 5-11             "
        except ValueError:
            self.notvalid = False 
            return "✘ Must Enter A Number"

    def level_verification(self):
        if self.player_lvl == "Select Level":
            self.notvalid = True
            return "✘ Level Required"
        else:
            self.notvalid = False 
            return "✔ Valid                              "              
            
    def write_file(self):
        results_file = open("math_results.text", "a")
        results_file.write("-------------------------\n")
        results_file.write(f"Student Name: {self.student_name} \n"
                            f"Year Level: {self.range} \n"
                            f"Operation: {self.difficulty}\n")
        
        results_file.write("-------------------------\n")
        results_file.close()
        
    
    