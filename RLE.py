a = input("Enter str: ")
encoded = ""
count = 1
for i in range(len(a)):
    if (i + 1 < len(a) and a[i] == a[i + 1]):
        count += 1
    else:
        encoded += a[i] + str(count)
        count = 1
print(encoded)