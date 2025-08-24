# Class 
class Student:
    # Data Properties / Constructor
    def __init__(self, name, roll, grade):

        ## These are all propertie/ attributes/ behavior of Student Class
        self.name = name
        self.roll = roll
        self.grade = grade

    # Functional Properties / Method:
    def display_info(self):             # Which to Show (Ans: Class Properties, at a time so, self)
        print(f"Name :{self.name}, Roll:{self.roll}, Grade:{self.grade} ")

# Define Object out of class Block
s1 = Student("Maruf", 101,"A+")
s1.display_info()



