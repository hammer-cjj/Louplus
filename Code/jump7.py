def check7(x):
	while x > 0:
		if x % 10 == 7:
			return True
		x = x // 10
	return False

for i in range(1, 101):
	if i % 7 != 0 and not check7(i):
		print(i)