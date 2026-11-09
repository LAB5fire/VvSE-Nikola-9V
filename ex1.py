n = int(input("Enter number: "))
if n <= 0:
    print("Невалиден брой")
else:
    count = 0
    total = 0
    count_pos = 0
    for i in range(0, n):
        number = int(input("Enter num"))
        if number % 3 == 0:
            count += 1
        if number > 0:
            total += number
            count_pos += 1
    print("Кратни на 3:", count)
    if total != 0:
        average = total / count_pos
        print("Average:", round(average, 2))
    else:
        print("Няма положителни")