# wapp to read marks from the user 
# count 1. > 80 2. > 60 3. remaining

marks = []
res = input(" do u want to enter some marks y/n ")
while res == "y":
	m = int(input("enter marks "))
	marks.append(m)
	res = input("do u want to enter more y/n ")

c1, c2, c3 = 0, 0, 0

for m in marks:
	if m > 80:
		c1 = c1 + 1
	elif m > 60:
		c2 = c2 + 1
	else:
		c3 = c3 + 1
print(c1, c2, c3)
