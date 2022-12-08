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


def add_it_up(student_list):
    sum = 0
    for student in student_list:
        this_student_credits = student.credits
        sum = sum + this_student_credits
    return sum


def add_it_with_recursion(student_list):
    if student_list == []:
        return 0
    current_student = student_list[0]
    return current_student.credits + add_it_with_recursion(student_list[1:])


def find_average_gpa(student_list):
    total_gpa = 0
    numbers_of_students = len(student_list)
    for student in student_list:
        current_student_GPA = student.GPA
        total_gpa += current_student_GPA
    return total_gpa/numbers_of_students


def find_median(student_list):
    if len(student_list) == 1:
        return student_list[0]
    if len(student_list) == 2:
        student1 = student_list[0]
        student2 = student_list[1]
        return (student1.credits + student2.credits)/2
    return find_median(student_list[1:-1])


data = load_data("students.txt")
#sort later
data.sort(key=get_key)
result = find_median(data)
print(f"the student with the median credits was {result}")
#data = load_data("students.txt")
#result = find_average_gpa(data)
#print(f"the average gpa was {result}")



#data = load_data("students.txt")
#result = add_it_up(data)
#result2 = add_it_with_recursion(data)
#print(f"Those students took {result} credit so far")
#print(f"and calculated with recursion we get {result2}")


#main()
