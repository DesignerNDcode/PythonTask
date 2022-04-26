class students:
    student_name = 'Muhaimin'
    student_marks = 55.5


# objects===============
student = students
# objects===============

print("Before ======", student.student_name, "is student  with marks", student.student_marks)

# modification=================
student.student_name = input("Enter your name #1")
student.student_marks = float(input("Enter your marks #1"))
# modification=================

print("Know ======", student.student_name, "is student  with marks", student.student_marks)
