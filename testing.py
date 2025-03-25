str1 = "hello"
str2 = "wassup"

mystrs = [str2, str1]
print(mystrs)
mystrs = sorted(mystrs, key=lambda x: len(x))
print(mystrs)

for line in zip(*mystrs):
    print(" ".join(line))