def near(removeLetter, match):
    for i in range(len(removeLetter)):
        front = removeLetter[:i]
        back = removeLetter[i+1:]
        newWord = front + back
        if newWord == match:
            return True
    return False

print(near("reset", "rest"))
print(near("dragoon", "dragon"))
print(near("eave", "leave"))
print(near("sleet", "lets"))
