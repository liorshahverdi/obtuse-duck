def calculate_fine(actual, expected):
	actual_prp = actual.split()
	actual_day, actual_month, actual_year = int(actual_prp[0]), int(actual_prp[1]), int(actual_prp[2])
	expected_prp = expected.split()
	expected_day, expected_month, expected_year = int(expected_prp[0]), int(expected_prp[1]), int(expected_prp[2])
	if actual_year <= expected_year:
		if actual_month <= expected_month:
			if actual_day <= expected_day:
				print 0
			else:
				day_diff = actual_day - expected_day
				print 15 * day_diff
		else:
			month_diff = actual_month - expected_month
			print 500 * month_diff
	else:
		print 10000

calculate_fine('2 7 1014', '1 1 1015')
#calculate_fine('28 2 2015', '15 4 2015') 