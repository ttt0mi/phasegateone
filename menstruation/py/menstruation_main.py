import menstruation
from menstruation import *

months = {"January" : 1, "February" : 2, "March" : 3, "April" : 4, "May" : 5, "June" : 6, "July" : 7, "August" : 8, "September" : 9, "October" : 10, "November" : 11, "December" : 12}


while True:
	info = information(months)
	
	if not isinstance(info, tuple):
		print(info)
		continue

	ovulation = get_ovulation(info)
	wind_start, wind_end = get_fertility_window(info)
	p_start, p_end = get_next_period(info)

	print()
	print(f"we predict your ovulation day will be on {ovulation}")
	print(f"we predict your fertility window is between {wind_start} to {wind_end}")
	print(f"we predict your next period will be between {p_start} to {p_end}")
	break


print("bye")