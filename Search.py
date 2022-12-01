class Student :
    def __init__(self, bannerId, gpa, credits_earned, name):
        self.studentId = bannerId
        self.GPA = gpa
        self.credits = credits_earned
        self.name = name


    def __str__(self):
        return f"student {self.name} with gpa: {self.GPA}\ncredits: {self.credits}\nstudent ID: {self.studentId}\n"


def load_data(file_name):
    student_list =[]
    student_file = open("students.txt")
    student_lines = student_file.readlines()
    for line in student_lines:
        split_line = line.split('|')
        current_student = Student(split_line[1],
                                  float(split_line[3]),
                                  int(split_line[2]),
                                  split_line[0])
        student_list.append(0,current_student)
    return student_list


def main():
    data = load_data("students.txt")
    #sort here later
    for student in data:
        print(student)

main()

