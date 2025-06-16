def test_questions():

	questions = [
	{"A": "expand energy, enjoy groups", "B": "conserve energy, enjoy one-on-ones"},
	{"A": "Interpret literally", "B": "look for meaning and possibilities"},
	{"A": "logical, thinking, questioning", "B": "empathetic, feeling, accommodating"},
	{"A": "organised, orderly", "B": "flexible, adaptable"},
	{"A": "more outgoing, think out loud", "B": "more reserved, think to yourself"},
	{"A": "practical, realistic, experiential", "B": "imaginative, innovative, theoretical"},
	{"A": "candid, straight forward, frank", "B": "tactful, kind, encouraging"},
	{"A": "plan, schedule", "B": "unplanned, spontaneous"},
	{"A": "seek many tasks, public activities, interaction with others", "B": "seek private, solitary activities with quiet to concentrate"},
	{"A": "standard, usual, conventional", "B": "different, novel, unique"},
	{"A": "firm, tend to criticise, hold the line", "B": "gentle, tend to appreciate, conciliate"},
	{"A": "regulated, structured", "B": "easy-going, live and let live"},
	{"A": "external, communicative, express yourself", "B": "internal, reticent, keep to yourself"},
	{"A": "focus on here-and-now", "B": "look to the future, global perspective, big picture"},
	{"A": "tough-minded, just", "B": "tender-hearted, merciful"},
	{"A": "preparation, plan ahead", "B": "go with the flow, adapt as you go"},
	{"A": "active, initiate", "B": "reflective, deliberate"},
	{"A": "facts, things, what is", "B": "ideas, dreams, what could be, philosophical"},
	{"A": "matter of fact, issue-oriented", "B": "sensitive, people-oriented, compassionate"},
	{"A": "control, govern", "B": "latitude, freedom"}]

	return questions



def name_check(name):

	invalids = (" ", "-", "'")
	temp = name.replace("-", "").replace(" ", "").replace("'", "")

	if not name or name.isspace(): return False
	if name.startswith(invalids) or name.endswith(invalids): return False
	if len(temp) not in range(2, 41): return False
	if temp.isalnum(): return True
	else: return False



def energy_questions(questions, selection, counters, answers, name):

	E_count, I_count = counters

	match selection:
		case 1:
			while True:
				print(f"\nA. {questions[0]['A']}")
				print(f"B. {questions[0]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						E_count += 1
						break
					case "B":
						I_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[0][choice]}")
			return (E_count, I_count)


		case 2:
			while True:
				print(f"\nA. {questions[4]['A']}")
				print(f"B. {questions[4]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						E_count += 1
						break
					case "B":
						I_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[4][choice]}")
			return (E_count, I_count)


		case 3: 
			while True:
				print(f"\nA. {questions[8]['A']}")
				print(f"B. {questions[8]['B']}")
				
				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						E_count += 1
						break
					case "B":
						I_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[8][choice]}")
			return (E_count, I_count)


		case 4:
			while True:
				print(f"\nA. {questions[12]['A']}")
				print(f"B. {questions[12]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						E_count += 1
						break
					case "B":
						I_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[12][choice]}")
			return (E_count, I_count)


		case 5:
			while True:
				print(f"\nA. {questions[16]['A']}")
				print(f"B. {questions[16]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						E_count += 1
						break
					case "B":
						I_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[16][choice]}")
			return (E_count, I_count)


		case 6:
			print()
			print(f"hey {name}. you chose:")
			for item in answers:
				print(item)

			print(f"No of As selected: {E_count}")
			print(f"No of Bs selected: {I_count}\n")

			return "E" if E_count > I_count else "I"

		case _:
			pass




def cognitive_questions(questions, selection, counters, answers):

	S_count, N_count = counters

	match selection:
		case 1:
			while True:
				print(f"\nA. {questions[1]['A']}")
				print(f"B. {questions[1]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						S_count += 1
						break
					case "B":
						N_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[1][choice]}")
			return (S_count, N_count)


		case 2:
			while True:
				print(f"\nA. {questions[5]['A']}")
				print(f"B. {questions[5]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						S_count += 1
						break
					case "B":
						N_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[5][choice]}")
			return (S_count, N_count)


		case 3: 
			while True:
				print(f"\nA. {questions[9]['A']}")
				print(f"B. {questions[9]['B']}")
				
				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						S_count += 1
						break
					case "B":
						N_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[9][choice]}")
			return (S_count, N_count)


		case 4:
			while True:
				print(f"\nA. {questions[13]['A']}")
				print(f"B. {questions[13]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						S_count += 1
						break
					case "B":
						N_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[13][choice]}")
			return (S_count, N_count)


		case 5:
			while True:
				print(f"\nA. {questions[17]['A']}")
				print(f"B. {questions[17]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						S_count += 1
						break
					case "B":
						N_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[17][choice]}")
			return (S_count, N_count)


		case 6:
			print()
			for item in answers:
				print(item)

			print(f"No of As selected: {S_count}")
			print(f"No of Bs selected: {N_count}\n")

			return "S" if S_count > N_count else "N"


		case _:
			pass



def value_questions(questions, selection, counters, answers):

	T_count, F_count = counters

	match selection:
		case 1:
			while True:
				print(f"\nA. {questions[2]['A']}")
				print(f"B. {questions[2]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						T_count += 1
						break
					case "B":
						F_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[2][choice]}")
			return (T_count, F_count)


		case 2:
			while True:
				print(f"\nA. {questions[6]['A']}")
				print(f"B. {questions[6]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						T_count += 1
						break
					case "B":
						F_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[6][choice]}")
			return (T_count, F_count)


		case 3: 
			while True:
				print(f"\nA. {questions[10]['A']}")
				print(f"B. {questions[10]['B']}")
				
				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						T_count += 1
						break
					case "B":
						F_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[10][choice]}")
			return (T_count, F_count)


		case 4:
			while True:
				print(f"\nA. {questions[14]['A']}")
				print(f"B. {questions[14]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						T_count += 1
						break
					case "B":
						F_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[14][choice]}")
			return (T_count, F_count)


		case 5:
			while True:
				print(f"\nA. {questions[18]['A']}")
				print(f"B. {questions[18]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						T_count += 1
						break
					case "B":
						F_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[18][choice]}")
			return (T_count, F_count)


		case 6:
			print()
			for item in answers:
				print(item)

			print(f"No of As selected: {T_count}")
			print(f"No of Bs selected: {F_count}\n")

			return "T" if T_count > F_count else "F"


		case _:
			pass




def life_questions(questions, selection, counters, answers):

	J_count, P_count = counters

	match selection:
		case 1:
			while True:
				print(f"\nA. {questions[3]['A']}")
				print(f"B. {questions[3]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						J_count += 1
						break
					case "B":
						P_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[3][choice]}")
			return (J_count, P_count)


		case 2:
			while True:
				print(f"\nA. {questions[7]['A']}")
				print(f"B. {questions[7]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						J_count += 1
						break
					case "B":
						P_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[7][choice]}")
			return (J_count, P_count)


		case 3: 
			while True:
				print(f"\nA. {questions[11]['A']}")
				print(f"B. {questions[11]['B']}")
				
				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						J_count += 1
						break
					case "B":
						P_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[11][choice]}")
			return (J_count, P_count)


		case 4:
			while True:
				print(f"\nA. {questions[15]['A']}")
				print(f"B. {questions[15]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						J_count += 1
						break
					case "B":
						P_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[15][choice]}")
			return (J_count, P_count)


		case 5:
			while True:
				print(f"\nA. {questions[19]['A']}")
				print(f"B. {questions[19]['B']}")

				choice = str(input("A or B: ")).upper()

				match choice:
					case "A":
						J_count += 1
						break
					case "B":
						P_count += 1
						break
					case _:
						print("invalid choice")
						continue

			answers.append(f"{choice}. {questions[19][choice]}")
			return (J_count, P_count)


		case 6:
			print()
			for item in answers:
				print(item)

			print(f"No of As selected: {J_count}")
			print(f"No of Bs selected: {P_count}\n")

			return "J" if J_count > P_count else "P"


		case _:
			pass




def type(*personalities):
	
	personality = "".join(personalities)

	match personality:

		case "INFP":
			print("""
your personality type: INFP
known as The Healer,
The Thoughtful Idealist (MBTI),
The Mediator (16Personalities), etc
	
read more about your personality here:
www.truity.com/blog/personality-type/infp
			""")
			return "INFP"



		case "INTJ":
			print("""
your personality type: INTJ

known as The Mastermind,
The Conceptual Planner (MBTI)
The Architect (16Personalities), etc
	
read more about your personality here:
www.truity.com/blog/personality-type/intj
			""")
			return "INTJ"



		case "INFJ":
			print("""
your personality type: INFJ

known as The Counsellor,
The Insightful Visionary (MBTI)
The Advocate (16Personalities), etc
	
read more about your personality here:
www.truity.com/blog/personality-type/infj
			""")
			return "INFJ"



		case "INTP":
			print("""
your personality type: INTP

known as The Architect,
The Objective Analyst (MBTI)
The Logician (16Personalities)
	
read more about your personality here:
www.truity.com/blog/personality-type/intp
			""")
			return "INTP"



		case "ENFP":
			print("""
your personality type: ENFP

known as The Champion,
The Imaginative Motivator (MBTI)
The Campaigner (16Personalities)
	
read more about your personality here:
www.truity.com/blog/personality-type/enfp
			""")
			return "ENFP"



		case "ENTJ":
			print("""
your personality type: ENTJ

known as The Commander
	
read more about your personality here:
www.truity.com/blog/personality-type/entj
			""")
			return "ENTJ"



		case "ENTP":
			print("""
your personality type: ENTP

known as The Visionary
	
read more about your personality here:
www.truity.com/blog/personality-type/entp
			""")
			return "ENTP"



		case "ENFJ":
			print("""
your personality type: ENFJ

known as The Teacher
	
read more about your personality here:
www.truity.com/blog/personality-type/enfj
			""")
			return "ENFJ"



		case "ISFJ":
			print("""
your personality type: ISFJ

known as The Protector
	
read more about your personality here:
www.truity.com/blog/personality-type/isfj
			""")
			return "ISFJ"



		case "ISFP":
			print("""
your personality type: ISFP

known as The Composer
	
read more about your personality here:
www.truity.com/blog/personality-type/isfp
			""")
			return "ISFP"



		case "ISTJ":
			print("""
your personality type: ISTJ

known as The Inspector
	
read more about your personality here:
www.truity.com/blog/personality-type/istj
			""")
			return "ISTJ"



		case "ISTP":
			print("""
your personality type: ISTP

known as The Craftsperson
	
read more about your personality here:
www.truity.com/blog/personality-type/istp
			""")
			return "ISTP"



		case "ESFJ":
			print("""
your personality type: ESFJ

known as The Provider
	
read more about your personality here:
www.truity.com/blog/personality-type/esfj
			""")
			return "ESFJ"



		case "ESFP":
			print("""
your personality type: ESFP

known as The Performer
	
read more about your personality here:
www.truity.com/blog/personality-type/esfp
			""")
			return "ESFP"



		case "ESTJ":
			print("""
your personality type: ESTJ

known as The Supervisor
	
read more about your personality here:
www.truity.com/blog/personality-type/estj
			""")
			return "ESTJ"



		case "ESTP":
			print("""
your personality type: ESTP

known as The Dynamo
	
read more about your personality here:
www.truity.com/blog/personality-type/estp
			""")
			return "ESTP"













