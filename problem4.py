print("Code for Problem 4")
dup = [1,1,2,3,4,64,35,93,35,87,4,3]
res = []
for i in dup:
	if i not in res:
		res.append(i)
print(res)