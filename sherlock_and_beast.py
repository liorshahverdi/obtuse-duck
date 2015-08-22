'''
https://www.hackerrank.com/challenges/sherlock-and-the-beast
 A 'Decent Number' has the following properties:
 	1. 	3,5, or both as its digits. No other digit is allowed.
 	2. 	Number of times 3 appears is divisible by 5.
 	3. 	Number of times 5 appears is divisible by 3.
'''
num_test_cases = int(raw_input())
for i in range(num_test_cases):
	num_str = str(raw_input())
	if not num_str.__contains__('5') and not num_str.__contains__('3'):
		print 'not valid'