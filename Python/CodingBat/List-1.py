def first_last6(nums): #Checks to see if 6 is at the start or end or the array
  return nums[0] == 6 or nums[-1] == 6
print("\nfirst_last6")
print(first_last6([1, 2, 3, 4, 5, 6]))

def same_first_last(nums): #Checks if a array is more than 1 length and if the first and last number are the same
  return len(nums) >= 1 and (nums[0] == nums[-1])
print("\nsame_first_last")
print(same_first_last([1, 2, 2, 3, 1]))

def make_pi(): # Returning an array
  return [3, 1, 4]
print("\nmake_pi ")

def common_end(a, b):#Check if the arrays have the same first or last number
  return (a[0] == b[0]) or (a[-1] == b[-1])
print("\ncommon_end")
print(common_end([1, 2, 3], [7, 3]))

def sum3(nums):# Totals the values in the array
  total = 0
  for i in range(len(nums)):
    total = total + nums[i]
  return total
print("\nsums3")
print(sum3([1, 2, 3]))

def rotate_left3(nums): # Rotates the array
  return [nums[1], nums[2], nums[0]]
print("\nrotate_left3")
print(rotate_left3([1, 2, 3]))

def reverse3(nums): #Reverses the array
  return [nums[2], nums[1], nums[0]]
print("\nreverse3")
print(reverse3([1, 2, 3]))

def max_end3(nums): # Compares first and last value, returns array of max value
  maxVal = max(nums[0], nums[-1])
  return [maxVal, maxVal, maxVal]
print("\nmax_end3")
print(max_end3([1, 2, 3]))

def sum2(nums): # Returns a sum of the first 2 numbers or less
  if len(nums) == 0:
    return 0
  elif len(nums) == 1:
    return nums[0]
  else:
    return nums[0] + nums[1]
print("\nsum2")
print(sum2([1, 2, 3]))

def middle_way(a, b): ## Returns the middle element of 2 arrays
  return [a[1], b[1]]
print("\nmiddle_way")
print(middle_way([1, 2, 3], [4, 5, 6]))

def make_ends(nums):# Returns an array with the first and last number
  return [nums[0], nums[-1]]
print("\nmake_ends")
print(make_ends([7, 4, 6, 2]) → [7, 2])

def has23(nums): # Checks if an array has 2 or 3
  for i in range(len(nums)):
    if nums[i] == 2 or nums [i] == 3:
      return True
  return False
print("\nhas23")
print(has23([2, 5]))







