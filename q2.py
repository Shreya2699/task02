Str=input("enter a string with combination of upper & lower case")
words = Str.split()
lower = []
upper = []
for char in Str:
    if char.islower():
        lower.append(char)
    else:
        upper.append(char)
sorted = ''.join(lower + upper)
print("\n arranging characters giving precedence to lowercase letters:")
print(sorted)