a = int(input("Enter positive a: "))
b = int(input("Enter positive b: "))
if a > b:
    temp = a
    a = b
    b = temp
is_perfect = 0
count = 0
line = ""
for i in range(a, b + 1):
    total = 0
    for j in range (1, i):
        if i % j == 0:
            total += j
    if i == total:
        line += str(i) + " "
        is_perfect = 1
    elif total > i:
        count += 1
if is_perfect == 0:
    print("No perfects")
print(line)
print("Изобилни:", count)
