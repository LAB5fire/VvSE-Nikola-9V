a = input("Enter encoded str: ")
decoded = ""
i = 0
while i < len(a):
    decoded += a[i] * int(a[i + 1])
    i += 2
print(decoded)