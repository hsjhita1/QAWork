input = input("Enter words seperated by , : ")
input = input.strip()
words = input.split(',')
words.sort()
for i in range(len(words)):
    print(words[i], end=",")