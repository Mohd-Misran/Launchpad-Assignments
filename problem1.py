print("Code for Problem 1")

name = input("Enter your name: ")
age = input("Enter your age: ")
age = int(age)
year = 2019
year = int(year)
for i in range(len(name)):
	if name[i] == " ":
		first_name = name[0:i]
s = f"Hey {first_name} ! You'll turn 100 years old in {year+100-age}"
print(s)