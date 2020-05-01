isbn = input("Input ISBN without check digit: ")
listISBN = [int(x) for x in str(isbn)]
print(listISBN)
sum = 0
for i in range(1, len(listISBN) + 1):
    if i % 2 != 0:
        sum = sum + listISBN[i-1]
        print(sum)
    elif i % 2 == 0:
        sum = sum + (listISBN[i-1] * 3)
        print(sum)
checkDigit = 10 - (sum%10)
print(checkDigit)