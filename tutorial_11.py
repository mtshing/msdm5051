# __all__ = ["code", "Student"]

code = 5051

def get_course():
	print("My course is　MSDM5051")
	
class Student:
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        
    def study(self):
        print(self.name, " is studying hard. He gets a ", self.grade, " in this course.")
		
		
