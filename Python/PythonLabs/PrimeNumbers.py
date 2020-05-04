maxLimit = int(input("Enter max number: "))
for i in range(1, maxLimit + 1):
    for j in range(2, i):
        if i % j == 0:
            break
    else:
        print(i)