
def teacher_details():

	print("welcome to hell")
	while True:
		try:
			student_no = int(input("How many students you got? "))
			
			if student_no < 1: raise ValueError("stop messing about mate")

			subject_no = int(input("How many subjects each of 'em got? "))
	
			if subject_no < 1: raise ValueError("stop messing about mate")
			
		except ValueError as e:
			print(f"{e}, try again\n")
			continue
		print()
		return (student_no, subject_no)
		



def student_details(outer_size, inner_size):

	grades = {}
	
	for count in range(1, outer_size + 1):
		
		scores , i = [], 1

		while i <= inner_size:
			try:
				print(f"entering score for student {count}")
				score = int(input(f"score in subject {i}: "))
				if score not in range(101):
					raise ValueError("score can only be between 0 - 100")

			except ValueError as e:
				print(f"{e}, try again")
				continue

			print(f"saving {'>' * 20}\nsaved successfully\n")

			scores.append(score)
			i += 1

		total = sum(scores)
		average = round(total / len(scores), 2)
		scores.extend([total, average])
	
		grades[f"student {count}"] = scores

	averages = sorted([item[len(item)-1] for item in grades.values()], reverse=True)

	for item in grades.values():
		for pos, avg in enumerate(averages, 1):
			if item[len(item)-1] == avg: item.append(pos)
		
	return grades





def table(grades):
	columns = len(grades["student 1"])

	header = ""
	student_details = ""

	header += "STUDENT\t\t"
	for i in range(1, columns - 2):
		header += f"SUB{i}\t"
	header += "TOTAL\tAVG\tPOS"

	for student, details in grades.items():
		student_details += f"{student}\t"
		for i in range(len(details)):
			student_details += f"{details[i]}\t"
		student_details += "\n"


	my_table = f"""
{'=' * columns * 10}
{header}
{'=' * columns * 10}
{student_details}
{'=' * columns * 10}
{'=' * columns * 10}
	"""

	return my_table

	




def subject_summary(grades):

	subject_columns = len(grades["student 1"]) - 3

	highest_passes, highest_passes_subj, lowest_fails, lowest_fails_subj = -1, " ", -1, " "
	
	subj_sum = ""

	for i in range(subject_columns):
		max, max_name, min, min_name = 0, " ", 1000 ** 1000, " "
		sum, passes, fails = 0, 0, 0

		for student, details in grades.items():
			if details[i] > max:
				max = details[i] 
				max_name = student

			elif details[i] == max: max_name = max_name + " & " + student

			if details[i] < min:
				min = details[i] 
				min_name = student

			elif details[i] == min: min_name = min_name + " & " + student 

			sum += details[i]

			if details[i] > 49: passes += 1
			else: fails += 1

		average = round(sum/len(grades), 2)
		hss = f"{max_name} scoring {max}"
		lss = f"{min_name} scoring {min}"

		subj_sum += f"""
subject {i + 1}
highest scoring student is: {hss}
lowest scoring student is: {lss}
total score is: {sum}
average score is: {average}
number of passes : {passes}
number of fails : {fails}
		"""

		if passes > highest_passes:
			highest_passes = passes
			highest_passes_subj = f"subject {i + 1}"

		elif passes == highest_passes: highest_passes_subj = highest_passes_subj + " & " + f"subject {i + 1}"

		if fails > lowest_fails:
			lowest_fails = fails
			lowest_fails_subj = f"subject {i + 1}"

		elif fails == lowest_fails: lowest_fails_subj = lowest_fails_subj + " & " + f"subject {i + 1}"



	return [subj_sum, highest_passes, highest_passes_subj, lowest_fails, lowest_fails_subj]







def class_summary(grades, array):

	subject_columns = len(grades["student 1"]) - 3
	max, max_name, min, min_name = 0, " ", 1000 ** 1000, " "
	max_subj, min_subj = " ", " "
	total, average = 0, 0

	highest, highest_name, lowest, lowest_name = 0, " ", 1000 ** 1000, " "

	for student, details in grades.items():
		sum = 0

		for i in range(subject_columns):
			if details[i] > max:
				max = details[i] 
				max_name = student
				max_subj = f"subject {i + 1}"

			elif details[i] == max:
				max_name = max_name + " & " + student
				max_subj = max_subj + " & " + f"subject {i + 1}" 

			if details[i] < min:
				min = details[i] 
				min_name = student
				min_subj = f"subject {i + 1}"

			elif details[i] == min:
				min_name = min_name + " & " + student
				min_subj = min_subj + " & " + f"subject {i + 1}" 

			sum += details[i]

		average += round(sum/len(grades), 2)
		total += sum

		if sum > highest:
			highest = sum
			highest_name = student

		elif sum == highest: highest_name = highest_name + " & " + student

		if sum < lowest:
			lowest = sum
			lowest_name = student

		elif sum == lowest: lowest_name = lowest_name + " & " + student	

	
	class_sum = f"""
The hardest subject is {array[4]} with a failure count of {array[3]} 
The easiest subject is {array[2]} with a pass count of {array[1]} 
The overall highest score is scored by {max_name} in {max_subj} scoring {max}
The overall lowest score is scored by {min_name} in {min_subj} scoring {min}
{'=' * 50}

CLASS SUMMARY
{'=' * 50}
best graduating student is: {highest_name} scoring {highest}
{'=' * 50}

{'!' * 50}
worst graduating student is: {lowest_name} scoring {lowest} 
{'!' * 50}

{'=' * 50}
class total score is: {total}
class average score is: {average}
{'=' * 50}
	"""

	return class_sum


	



















