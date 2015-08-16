num_test_cases = int(raw_input())
for i in range(num_test_cases):
	test_str = str(raw_input())
	test_prop = test_str.split()
	n, k = int(test_prop[0]), int(test_prop[1]) #k student must be on time
	case = str(raw_input())
	case_prop = case.split()
	on_time = 0
	for num in case_prop:
		number = int(num)
		if number <= 0:
			on_time += 1
	if k > on_time:
		print 'YES'
	else:
		print 'NO'