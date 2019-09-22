print("Code for Problem 3")
numbers = [2,5,6,15,6,24,33,19,6,89,6]
ind = []
ele = input("Enter element to be searched: ")
ele = int(ele)
for index,value in enumerate(numbers):
	if value==ele:
		ind.append(index)
print(ind)