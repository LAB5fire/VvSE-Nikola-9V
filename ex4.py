n = int(input("Enter number:"))

def is_prime(number):
    square_root = round(number ** 0.5)
    for j in range(2, square_root + 1):
        if number % j == 0:
            return False
    return True

while n < 5:
    n = int(input("Enter number:"))
count = 0
biggest = 0
for p in range(2, n - 1):
    if is_prime(p) and is_prime(p + 2):
        print(p, p + 2)
        count += 1
        biggest = p

print("Count:", count)
print("Biggest:", biggest, biggest + 2)