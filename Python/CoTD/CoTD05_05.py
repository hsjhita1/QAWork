number = int(input("Enter your number: "))
fac = 1
if number < 0:
    print("Invalid number")
elif number == 0:
    print(number, " factorial is ",fac)
else:
    for i in range(1, number + 1):
        fac = fac * i
    print(number, " factorial is ", fac)