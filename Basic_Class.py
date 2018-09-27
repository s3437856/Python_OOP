# Basic OOP
class Student:
    """
    THe Student class defines a student in terms of full name, sex and gpa.
    """
    def __init__(self, first_name, last_name, sex, gpa):
        self.first_name = first_name
        self.last_name = last_name
        self.sex = sex
        self.gpa = gpa
        
    def get_name(self):
        return 'Full Name: ' + self.first_name + ' ' + self.last_name
    
    def get_sex(self):
        return 'Sex: ' + self.sex
    
    def get_gpa(self):
        return 'GPA: ' + self.gpa
        
    def get_all(self):
        return Student.get_name(self) + '\n' + Student.get_sex(self) + '\n' \
               + Student.get_gpa(self)
    
    
def main():
    student_1 = Student('David', 'Diaz', 'Male', '3')
    print(isinstance(student_1, Student))
    print(student_1.get_all())


if __name__ == '__main__':
    main()
