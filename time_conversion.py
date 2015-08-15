def to_24_hour_format(oldtime):
	chars = list(oldtime)
	h = chars[:2]
	hr = int("".join(h))
	m = chars[3:5]
	s = chars[6:8]
	ap = chars[8:11]
	ampm = "".join(ap)
	if ampm == "PM":
		if hr != 12:
			hr += 12
	if ampm == "AM":
		if hr == 12:
			hr = '00'
		elif hr < 10:
			hr = '0'+str(hr)
	print str(hr)+':'+"".join(m)+':'+"".join(s)

to_24_hour_format('12:45:54PM')