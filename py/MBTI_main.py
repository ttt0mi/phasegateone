import MBTI
from MBTI import *


questions = test_questions()

energy_answers = []
cognitive_answers = []
value_answers = []
life_answers = []

energy = (0, 0)
cognitive = (0, 0)
value = (0, 0)
life = (0, 0)


print("Welcome to the terrorism test")

while True:
	name = str(input("what is your name? "))

	if not name_check(name):
		print("invalid name, try again")
		continue

	print("Choose below what option most describes you")

	for selection in range(1, 7):
		energy = energy_questions(questions, selection, energy, energy_answers, name)
		cognitive = cognitive_questions(questions, selection, cognitive, cognitive_answers)
		value = value_questions(questions, selection, value, value_answers)
		life = life_questions(questions, selection, life, life_answers)


	type(energy, cognitive, value, life)
	break
