file = open("example_txt.txt", "r") ## r - read only, w - write only, r+ - read and write, a - append

print(file.readline()) ## Reads the current line and moves on, .read reads current line to end of file
file.readline()
print(file.readline())
file.seek(0) ## Start at the beginning of a file and go to character 0
print(file.readline())

lines = file.readlines() # Reads all lines
print(lines)

file.close()

file = open("writeExample.txt", "w") ## Create a new file in write only
for i in range(1, 11):
    newline = "This is line " + str(i) + "\n"
    file.write(newline) ## Writes a line to the file

file.close()

file = open("teams.txt", "w")
teams = ["Liverpool", "Manchester City", "Leicester City", "Chelsea", "Manchester United"]
for i in range(len(teams)):
    file.write(teams[i] + "\n")

file.close()

file = open("teams.txt", "r+")
file.write("This is a new line")
file.close()