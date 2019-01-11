def func(s):

	s = s.replace(" ", "")

	ct = {}

	for i in s:

		ct[i] = 0

	for i in s:

		ct[i] += 1

	odd_ct = 0

	for i in ct:

		if ct[i] % 2 != 0:

			odd_ct += 1

			if odd_ct > 1:

				return False

	return True


print(func("tact coa"))

print(func("Kaja"))


print(func("aja"))


print(func("malayalam"))

