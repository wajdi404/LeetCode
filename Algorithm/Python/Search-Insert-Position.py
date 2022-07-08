
def searchInsert( nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    
    low = 0
    high = len( nums ) - 1
    mid = 0

    while ( high >= low ):
        mid = (high + low) // 2
        if nums[mid] > target:
            high = mid - 1
        if nums[mid] < target:
            low = mid + 1
        if nums[mid] == target:
            return mid
    return high + 1

  
if __name__ == '__main__':
    nums = [1, 3, 5, 6]
    target =
    print(searchInsert( nums, target))
