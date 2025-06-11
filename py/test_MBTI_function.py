import MBTI
from MBTI import *
import unittest
from unittest import TestCase


class TestMBTIFunction(TestCase):

	questions = test_questions()
	name = "tomide"

	def test_MBTI_function1_Extrovert(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = energy_questions(self.questions, selection, counters, answers, self.name)
		personality = counters

		self.assertEqual(personality, "E", "choose extroverted options")



	def test_MBTI_function2_Sensing(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = cognitive_questions(self.questions, selection, counters, answers)
		personality = counters

		self.assertEqual(personality, "S", "choose sensing options")



	def test_MBTI_function3_Thinking(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = value_questions(self.questions, selection, counters, answers)
		personality = counters

		self.assertEqual(personality, "T", "choose thinking options")



	def test_MBTI_function4_Judging(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = life_questions(self.questions, selection, counters, answers)
		personality = counters

		self.assertEqual(personality, "J", "choose judging options")




	def test_MBTI_function5_Introvert(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = energy_questions(self.questions, selection, counters, answers, self.name)
		personality = counters

		self.assertEqual(personality, "I", "choose introverted options")



	def test_MBTI_function6_Intuitive(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = cognitive_questions(self.questions, selection, counters, answers)
		personality = counters

		self.assertEqual(personality, "N", "choose intuitive options")



	def test_MBTI_function7_Feeling(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = value_questions(self.questions, selection, counters, answers)
		personality = counters

		self.assertEqual(personality, "F", "choose feeling options")



	def test_MBTI_function8_Perceptive(self):
		counters = (0, 0)
		answers = []

		for selection in range(1, 7): 
			counters = life_questions(self.questions, selection, counters, answers)
		personality = counters

		self.assertEqual(personality, "P", "choose perceptive options")











