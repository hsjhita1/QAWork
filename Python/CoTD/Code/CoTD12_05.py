numbers = []
for i in range(1000, 3001):
    stringNum = str(i)
    if (int(stringNum[0]) % 2 == 0) and (int(stringNum[1]) % 2 == 0) and (int(stringNum[2]) % 2 == 0) and (int(stringNum[3]) % 2 == 0):
        numbers.append(stringNum)
for num in numbers:
    print(num, end=',')