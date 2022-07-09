
def twoSum( nums, target):
  """
  :type nums: List[int]
  :type target: int
  :rtype: List[int]
  """
# Solution using brute force
#   sum = []
#   for i in range(len(nums)):
#     for j in range(i+1,len(nums)):
#       if nums[i] + nums[j] == target:
#         sum.append(i)
#         sum.append(j)
#   return sum

# Solution using Hash table
  Dict = {}
  for i, n in enumerate(nums):
    if (target - n) in Dict:
      return [ i, Dict[target - n]]
    else:
      Dict[n] = i
  return []

if __name__ == '__main__':
  nums = [2,7,11,15] 
  target = 9
  t0 = time.time()
  print(twoSum( nums, target)) # output [0,1]
  t1 = time.time()
  print(t1 - t0)
