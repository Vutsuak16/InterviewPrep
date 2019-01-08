
def func(s):

	ct = {}

	for i in s:
		ct[i] = 0

	flg = 0

	for i in s:

		ct[i] += 1
		
		if ct[i] > 1:
			flg = 0
			break
		else:
			flg = 1

	if flg == 0:
		return 0
	return 1


ret = func("awd")

print(ret)