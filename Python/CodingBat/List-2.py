def count_evens(nums):
  count = 0
  for i in range(len(nums)):
    if nums[i] % 2 == 0:
      count = count + 1
  return count

def big_diff(nums):
  return max(nums) - min(nums)

def centered_average(nums):
  sum = 0
  for i in nums:
    sum = sum + i
  return (sum - min(nums) - max(nums)) / (len(nums)-2) 


def sum13(nums):
  sum = 0
  if len(nums) == 0:
    return 0
  for i in range(0, len(nums)):
    if nums[i] == 13:
      nums[i] = 0
      if i+1 < len(nums): 
        nums[i+1] = 0
    sum = sum + nums[i]
  return sum

def sum67(nums):
  sum = 0
  ignore = False
  for i in range(len(nums)):
    if nums[i] == 6:
      nums[i] = 0
      ignore = True
    elif ignore == True and nums[i] == 7:
      ignore = False
    elif ignore == False:
      sum = sum + nums[i]
  return sum

def has22(nums):
  for i in range(len(nums) - 1):
    if nums[i] == 2:
      if nums[i+1] == 2:
        return True
  return False
