import student_grades
from student_grades import *


no_of_students, no_of_subjects = teacher_details()

grades = student_details(no_of_students, no_of_subjects)

print(table(grades))

passes_fails = subject_summary(grades)

print(passes_fails[0])

print(class_summary(grades, passes_fails))