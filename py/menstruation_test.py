
p_month = str(input("what month did your last period occur? ")).lower().capitalize()

p_day = str(input("what day did it start?(in digits): "))

p_duration = str(input("On average, How long does it last(in days): "))

cycle = str(input("On average, how long is your menstrual cycle(in days): "))


period_month = period_month.lower()


ovulation_day = cycle_length / 2
fertile_window = ovulation_day - 5
fertile_window_end = ovulation_day + 1
next_period = last_period + cycle_length
next_period_end = next_period + period_days


if period_month in ("january", "march", "may",  "july", "august", "october", "december"):

	ovulation_day = (ovulation_day - 1) % 31 + 1
	fertile_window = (fertile_window - 1) % 31 + 1
	fertile_window_end = (fertile_window_end - 1) % 31 + 1
	next_period = (next_period - 1) % 31 + 1
	next_period_end = (next_period_end - 1) % 31 + 1


elif period_month in ("april", "june", "september",  "november"):

	ovulation_day = (ovulation_day - 1) % 30 + 1
	fertile_window = (fertile_window - 1) % 30 + 1
	fertile_window_end = (fertile_window_end - 1) % 30 + 1
	next_period = (next_period - 1) % 30 + 1
	next_period_end = (next_period_end - 1) % 30 + 1


elif  period_month == "february":

	ovulation_day = (ovulation_day - 1) % 28 + 1
	fertile_window = (fertile_window - 1) % 28 + 1
	fertile_window_end = (fertile_window_end - 1) % 28 + 1
	next_period = (next_period - 1) % 28 + 1
	next_period_end = (next_period_end - 1) % 28 + 1

