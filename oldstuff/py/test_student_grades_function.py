import student_grades
from student_grades import *
import unittest
from unittest import TestCase


class TestStudentGradesFunction(TestCase):

	grades = {"student 1": [67, 21, 49, 137, 45.67, 4], "student 2" : [98, 62, 56,216, 72.00, 2], "student 3" : [93, 34, 27, 154, 51.33, 3], "student 4" : [78, 83, 66, 227, 75.67, 1]}


	def test_student_grades_input_functions(self):
		student_no, subject__no = 4, 3		

		actual = teacher_details()
		expected = (student_no, subject__no)
		self.assertEqual(expected, actual)

		actual = student_details(student_no, subject__no)
		expected = self.grades		
		self.assertEqual(expected, actual, "enter grades according to test sample")




	def test_student_grades_table_function(self):

		actual = table(self.grades)
		expected = """
============================================================
STUDENT		SUB1	SUB2	SUB3	TOTAL	AVG	POS
============================================================
student 1	67	21	49	137	45.67	4	
student 2	98	62	56	216	72.0	2	
student 3	93	34	27	154	51.33	3	
student 4	78	83	66	227	75.67	1	

============================================================
============================================================
	"""

		self.assertMultiLineEqual(expected, actual)





	def test_student_grades_subject_summary_function(self):

		actual = subject_summary(self.grades)[0]
		expected = """
subject 1
highest scoring student is: student 2 scoring 98
lowest scoring student is: student 1 scoring 67
total score is: 336
average score is: 84.0
number of passes : 4
number of fails : 0
		
subject 2
highest scoring student is: student 4 scoring 83
lowest scoring student is: student 1 scoring 21
total score is: 200
average score is: 50.0
number of passes : 2
number of fails : 2
		
subject 3
highest scoring student is: student 4 scoring 66
lowest scoring student is: student 3 scoring 27
total score is: 198
average score is: 49.5
number of passes : 2
number of fails : 2
		"""

		self.assertMultiLineEqual(expected, actual)


	def test_student_grades_subject_summary_passes_fails(self):
		highest_passes = 4
		highest_passes_subject = "subject 1"
		lowest_fails = 2
		lowest_fails_subject = "subject 2 & subject 3"
		subj_summary = """
subject 1
highest scoring student is: student 2 scoring 98
lowest scoring student is: student 1 scoring 67
total score is: 336
average score is: 84.0
number of passes : 4
number of fails : 0
		
subject 2
highest scoring student is: student 4 scoring 83
lowest scoring student is: student 1 scoring 21
total score is: 200
average score is: 50.0
number of passes : 2
number of fails : 2
		
subject 3
highest scoring student is: student 4 scoring 66
lowest scoring student is: student 3 scoring 27
total score is: 198
average score is: 49.5
number of passes : 2
number of fails : 2
		"""

		actual = subject_summary(self.grades)
		expected = [subj_summary, highest_passes, highest_passes_subject, lowest_fails, lowest_fails_subject]

		self.assertEqual(expected, actual)






	def test_student_grades_class_summary_function(self):
		highest_passes = 4
		highest_passes_subject = "subject 1"
		lowest_fails = 2
		lowest_fails_subject = "subject 2 & subject 3"
		subj_summary = ""
	
		passes_fails = [subj_summary, highest_passes, highest_passes_subject, lowest_fails, lowest_fails_subject]
	
		actual = class_summary(self.grades, passes_fails)
		expected = """
The hardest subject is subject 2 & subject 3 with a failure count of 2 
The easiest subject is subject 1 with a pass count of 4 
The overall highest score is scored by student 2 in subject 1 scoring 98
The overall lowest score is scored by student 1 in subject 2 scoring 21
==================================================

CLASS SUMMARY
==================================================
best graduating student is: student 4 scoring 227
==================================================

!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
worst graduating student is: student 1 scoring 137 
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!

==================================================
class total score is: 734
class average score is: 183.5
==================================================
	"""
		
		self.assertMultiLineEqual(expected, actual)













