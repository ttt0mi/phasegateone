import menstruation
from menstruation import *
import unittest
from unittest import TestCase


class TestMenstruationFunction(TestCase):

	def test_menstruation_existence(self):
		month = 5
		day = 13
		duration = 4
		cycle = 28
		information = (month, day, duration, cycle)

		get_ovulation(information)
		get_fertility_window(information)
		get_next_period(information)


	def test_menstruation_day_check(self):
		month = "May"
		day = "13"

		self.assertTrue(day_check(day, month))


	def test_menstruation_cycle_check(self):
		cycle = "28"

		self.assertTrue(cycle_check(cycle))


	def test_menstruation_get_ovulation_date(self):
		month = 5
		day = 13
		duration = 4
		cycle = 28
		information = (month, day, duration, cycle)

		actual = get_ovulation(information)
		expected = "May 27"
		self.assertEqual(actual, expected)


	def test_menstruation_get_fertility_window(self):
		month = 5
		day = 13
		duration = 4
		cycle = 28
		information = (month, day, duration, cycle)

		actual = get_fertility_window(information)
		expected = ("May 22", "May 28")
		self.assertEqual(actual, expected)


	def test_menstruation_get_next_period(self):
		month = 5
		day = 13
		duration = 4
		cycle = 28
		information = (month, day, duration, cycle)

		actual = get_next_period(information)
		expected = ("June 10", "June 14")
		self.assertEqual(actual, expected)



