a = 5
b = 0

ct = 0

while a!= 0:

	x_a = a & 1
	x_b = b & 1

	if x_a != x_b:

		ct += 1
	a >>= 1
	b >>= 1 


print(ct)