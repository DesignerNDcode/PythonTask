class students:
    student_id = 42
    student_name = "Muhaimin"


# objects===============
student = students
# objects===============

student.student_class = "Python"

print("Before ===============", "id =", student.student_id, "name =", student.student_name, "class =", student.student_class)

del student.student_name

print("After ===============", "id =", student.student_id, "class =", student.student_class)
