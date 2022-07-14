
def findMedianSortedArrays( nums1, nums2):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :rtype: float
    """
    x = len(nums1)
    y = len(nums2)
    start = 0
    end = x
    posX = (end + start) // 2
    posY = ((x + y + 1) // 2) - posX
    while start <= end:
        PosLeftX = float('-inf') if posX == 0 else nums1[posX-1]
        PosRightX = float('inf') if posX == x else nums1[posX]
        PosLeftY = float('-inf') if posY == 0 else nums2[posY-1]
        PosRightY = float('inf') if posY == y else nums2[posY]

        if (PosLeftX <= PosRightY) and (PosLeftY <= PosRightX):
            if ((x + y) % 2 == 0):
                return ( ( max( PosLeftX, PosLeftY) + min(PosRightX, PosRightY) ) / 2)
            else:
                return max( PosLeftX, PosLeftY)
        elif PosLeftX > PosRightY:
            end = end - posX - 1
        else:
            start = posX + 1
        posX = (end + start) // 2
        posY = (( x + y + 1) // 2) - posX

if __name__ == '__main__':
    #nums1 = [ 1, 3, 8, 9, 15]
    #nums2 = [ 7, 11, 18, 19, 21, 25]
    # => merged array = [ 1, 3, 7, 8, 9, 11, 15, 18, 19, 21, 25] and median is 11.
    # nums1 = [1, 3]
    # nums2 = [2]
    # => merged array = [1,2,3] and median is 2.
    nums1 = [1, 2]
    nums2 = [3, 4]
    # => merged array = [1,2,3] and median is 2.
    print( findMedianSortedArrays( nums1, nums2))
