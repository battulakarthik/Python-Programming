a,b=raw_input().split()
if a.isdigit() and b.isdigit():
	a=int(a)
	b=int(b)
	s=0
	for i in range(a,b+1):
		if i%2!=0:
			s=s+i
	print s
else:
	print "Invalid"
