# String functions
def string_times(str, n): ## Returns a string 'n' amount of times
  text = ""
  for i in range(0, n):
    text = n * str
  return text
print("string_times")
print(string_times("Hello", 5))

def front_times(str, n): ## Truncates a string and repeats it 'n' number of times
  text = ""
  if len(str) < 3:
    text = n * str
  else:
    text = str[:3] * n
  return text
print("front_times")
print(front_times("Test", 4))

def string_bits(str): ## Returns every other character of a string
  text = ""
  for i in range(0, len(str), 2):
    text = text + str[i]
  return text
print("string_bits")
print(string_bits("Python"))

def string_splosion(str): ## Prints first letter, first 2 letters, first 3 ...
  text = ""
  for i in range(len(str) + 1):
    text = text + str[:i]
  return text
print("string_splosion")
print(string_splosion("Python"))

def last2(str): ## Finds the number of occurences of a substring in the text
  if len(str) < 2:
    return 0
  last2 = str[-2:]
  count = 0
  for i in range(len(str) - 2):
    substring = str[i:i+2]
    if substring == last2:
      count = count + 1
  return count
print("last2")
print(last2("hiaschiafafhi"))


## Array Functions
def array_count9(nums):## Checks the occureneces of '9' in the array
  count = 0
  for i in range(len(nums)):
    if nums[i] == 9:
      count = count + 1
  return count
print("array_count9")
print(array_count9([1, 3, 9, 9, 9]))

def array_front9(nums): ## Checks if a value occurs in a limited range
  arrayLength = len(nums)
  if arrayLength > 4:
    arrayLength = 4
  for i in range(arrayLength):
    if nums[i] == 9:
      return True
  return False
print("array_front9")
print(array_front9([1, 2, 3, 9, 9]))


def array123(nums):## Checks to see if 1,2,3 are in the array in that order
  for i in range(0, len(nums) - 2):
    if nums[i] == 1:
      if nums[i + 1] == 2:
        if nums[i + 2] == 3:
          return True
  return False
print("array123")
print(array123([1, 2, 3, 9, 9]))

def string_match(a, b): ## Checks if the same positions of 2 strings contains the same set of characters
  count = 0
  for i in range(len(a) - 1):
    if a[i:i+2] == b[i:i+2]:
      count = count + 1
  return count
print("string_match")
print(string_match("xxaaaz", "xxfsaz"))


