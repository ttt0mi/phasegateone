import datetime
import calendar

def month_check(month, months):

	if month not in months: return False
	return True



def day_check(day, month):
	
	if not day.isdecimal():
		return False

	day = int(day)

	list_31 = ["January", "March", "May",  "July", "August", "October", "December"]
	list_30 = ["April", "June", "September", "November"]
	list_28 = ["February"]

	if month in list_31:
		if day in range(1, 32): return True
		return False
	elif month in list_30:
		if day in range(1, 31): return True
		return False
	elif month in list_28:
		if day in range(1, 29): return True
		return False
	else: return False




def cycle_check(cycle):

	if not cycle.isdecimal(): return False
	return True
	
	


def information(months):
	print()
	#calendar.prcal(2025)
	print()

	p_month = str(input("what month did your last period occur? ")).lower().capitalize()

	if not month_check(p_month, months): return "invalid input"

	print()
	calendar.prmonth(2025, months[p_month])
	print()

	p_day = str(input("what day did it start?(in digits): "))
	if not day_check(p_day, p_month): return "invalid input"

	p_duration = str(input("On average, How long does it last(in days): "))
	if not cycle_check(p_duration): return "invalid input"

	cycle = str(input("On average, how long is your menstrual cycle(in days): "))
	if not cycle_check(cycle): return "invalid input"


	p_day = int(p_day)
	p_duration = int(p_duration)
	cycle = int(cycle)	

	return (months[p_month], p_day, p_duration, cycle)




def get_ovulation(dates):

	month, day, duration, cycle = dates

	period_start = datetime.date(2025, month, day)
	fol_phase = datetime.timedelta(cycle/2)
	ovulation_day = period_start + fol_phase
	
	return ovulation_day.strftime("%B %d")




def get_fertility_window(dates):
	
	month, day, duration, cycle = dates

	period_start = datetime.date(2025, month, day)
	fol_phase = datetime.timedelta(cycle/2)
	ovulation_day = period_start + fol_phase

	window_start = ovulation_day - datetime.timedelta(5)
	window_end = ovulation_day + datetime.timedelta(1)

	return (window_start.strftime("%B %d"), window_end.strftime("%B %d"))




def get_next_period(dates):
	
	month, day, duration, cycle = dates

	period_start = datetime.date(2025, month, day)
	menstrual_cycle = datetime.timedelta(cycle)
	next_period_start = period_start + menstrual_cycle
	next_period_end = next_period_start + datetime.timedelta(duration)

	return (next_period_start.strftime("%B %d"), next_period_end.strftime("%B %d"))




	






