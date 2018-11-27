a = ['Трепет', "свобода", "душа"]
s = ['awe', 'freedom', 'soul']
q = str()

for k in range (len(a)):	
	q = input(str(a[k]) + ": ")
	if q == s[k]:
		print("Yeah, that's right!\n")
	else:
		print("Ooops... Mistake!\n")