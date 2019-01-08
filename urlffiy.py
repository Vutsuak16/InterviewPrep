def func(s):

	space_count = 0

	for i in s:

		if i == ' ':
			space_count += 1

	truelength = space_count*2 + len(s)

	s2 = [0] * truelength

	index = len(s2) - 1

	for i in range(len(s)-1,-1,-1):

		if s[i] == ' ':

			s2[index] = '0'
			s2[index - 1] = '2'
			s2[index - 2] = '%'

			index -= 2

		else:

			s2[index] = s[i]

		index -= 1 


	S = ""

	for i in s2:

		S += i

	return S


print(func("Mr John Smith"))


















































































