def isPalindrome(x):
  """
  :type x: int
  :rtype: bool
  """
  r = 0
  y = abs(x)
  
  while(y != 0):
    r = (r * 10) + y % 10
    y = y // 10
  
  return True if r == x else False

if __name__ == '__main__':
  x = 123
  print(isPalindrome(x))
