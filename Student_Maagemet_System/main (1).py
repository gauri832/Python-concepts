from student import Student
from course import Course

def main():
    course = Course("Computer Science")

    s1 = Student("Asha", 1, 85)
    s2 = Student("Rahul", 2, 92)
    s3 = Student("Neha", 3, 70)

    course.add_student(s1)
    course.add_student(s2)
    course.add_student(s3)

    course.show_all_students()

    avg = course.calculate_average()
    print(f"Class Average Marks: {avg}")

    print("Total students:", Course.total_students)

if __name__ == "__main__":
    main()
