from student import Student

class Course:
    total_students = 0   # class attribute

    def __init__(self, course_name):
        self.course_name = course_name
        self.students = []   # list of Student objects

    def add_student(self, student):
        self.students.append(student)
        Course.total_students += 1
        print(f"Student {student.name} added to {self.course_name}")

    def remove_student(self, roll_no):
        for student in self.students:
            if student.roll_no == roll_no:
                self.students.remove(student)
                Course.total_students -= 1
                print(f"Student {student.name} removed")
                return
        print("Student not found")

    def show_all_students(self):
        if not self.students:
            print("No students enrolled")
            return

        print(f"\nStudents in {self.course_name}:")
        for student in self.students:
            student.display_info()
            print("Grade:", student.get_grade())
            print("-" * 20)

    def calculate_average(self):
        if not self.students:
            return 0

        total_marks = sum(student.marks for student in self.students)
        return total_marks / len(self.students)
