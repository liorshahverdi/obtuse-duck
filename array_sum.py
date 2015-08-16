size = int(raw_input())
list_str = str(raw_input())
mylist = list_str.split()
s = 0
for number in range(len(mylist)):
	n = int(mylist[number])
	s += n
print s