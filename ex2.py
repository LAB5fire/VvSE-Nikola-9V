n = int(input("Enter num: "))
if n == 0:
    print("Няма данни")
else:
    smallest = n
    last = n
    count_more_than_last = 0
    count = 0
    count_negative = 0
    while n != 0:
        count += 1
        if n < smallest:
            smallest = n
        if n > last:
            count_more_than_last += 1
        if n < 0:
            count_negative += 1
        n = int(input("Enter num: "))
    print("Smallest:", smallest)
    print("Нараствания:", count_more_than_last)
    percent = (count_negative/count)*100
    print("Отрицателни:", round(percent), "%")