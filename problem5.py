print("Code for Problem 5")
sent = input("Enter a sentence: ")
words = sent.split(" ")
rev = words[::-1]
res = ' '.join(rev)
res = res.capitalize()
print(res)