def func(s):

	flg = 1
	for i in range(len(s)):

		x =  s[i]

		for j in range(i+1 ,len(s)):

			if s[j] == x:
				flg = 0
				break
	
	if flg == 0:
		return 0
	else:
		return 1

ret = func("as")

print(ret)