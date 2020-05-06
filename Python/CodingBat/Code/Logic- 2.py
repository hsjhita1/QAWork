def make_bricks(small, big, goal): # See if its possible to make the goal with a set amount of bricks
  if int(goal / 5) <= big:
    if goal % 5 <= small:
      return True
    return False
  elif int(goal / 5) >= big:
    if goal - (big * 5) <= small:
      return True
    return False
print("make_bricks")
print(make_bricks(3, 1, 8))

def lone_sum(a, b, c):
  tempA = a
  tempB = b
  tempC = c
  if tempA == tempB:
    a = 0
    b = 0
  if tempA == tempC:
    a = 0
    c = 0
  if tempB == tempC:
    b = 0
    c = 0
  return a + b + c
print("\nlone_sum")
print(lone_sum(1, 2, 3))

def lucky_sum(a, b, c):
  if a == 13:
    return 0
  elif b == 13:
    return a
  elif c == 13:
    return a + b
  else:
    return a + b + c
print("\nlucky_sum")
print(lucky_sum(1, 2, 13))    

def no_teen_sum(a, b, c):
  return fix_teen(a) + fix_teen(b) + fix_teen(c)
  
def fix_teen(n):
  teenAges = [13, 14, 17, 18 , 19]
  for i in range(len(teenAges)):
    if n == teenAges[i]:
      return 0
  return n
print("\nno_teen_sum")
print(no_teen_sum(13, 14, 16))

def round_sum(a, b, c):
  return round10(a) + round10(b) + round10(c)
  
def round10(num):
  if num % 10 >= 5:
    return 10 + num - (num % 10)
  return num - (num % 10)
print("\nround_sum")
print(round_sum(14, 15, 19))

def make_chocolate(small, big, goal):
  if int(goal / 5) <= big:
    if goal - (int(goal / 5) * 5) <= small:
      return goal - (int(goal / 5) * 5)
  elif int(goal /5) > big:
    if goal - (big * 5) <= small:
      return goal - (big * 5)
  return -1
print("make_chocolate")
print(make_chocolate(4, 1, 9))