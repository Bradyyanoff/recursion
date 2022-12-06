class Student:
    def __init__(self, banner_id, gpa, credits_earned, name):
        self.studentId = banner_id
        self.GPA = gpa
        self.credits = credits_earned
        self.name = name

    def __str__(self):
        return f"student {self.name} with gpa: {self.GPA}\ncredits: " \
               f"{self.credits}\nstudent ID: {self.studentId}\n"


def load_data(load_file):
    student_list = []
    student_file = open("students.txt")
    student_lines = student_file.readlines()
    for line in student_lines:
        split_line = line.split('|')
        current_student = Student(split_line[1],
                                  float(split_line[3]),
                                  int(split_line[2]),
                                  split_line[0])
        student_list.insert(0, current_student)
    return student_list


def binary_search(student_list, students_to_find):
    if student_list == []:
        return None
    middle_location = len(student_list) // 2
    middle_student = student_list[middle_location]
    if middle_student.name == students_to_find:
        return middle_student
    if students_to_find < middle_student.name:
        return binary_search(student_list[:middle_location-1], students_to_find)
    else:
        return binary_search(student_list[middle_location+1:], students_to_find)


def get_key(student_to_sort):
    return student_to_sort.GPA


def main():
    data = load_data("students.txt")
    data.sort(key=get_key)
    student_name = input("who shall we look for")
    result = binary_search(data, student_name)
    print(result)
    #for student in data:
    #print(student)


main()
