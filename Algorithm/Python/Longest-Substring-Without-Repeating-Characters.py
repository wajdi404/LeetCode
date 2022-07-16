def lengthOfLongestSubstring( self, s):
  """
  :type s: str
  :rtype: int
  """
  maxleng = 0
  visited = {}
  start = 0
        
  for end in range(len(s)):
    if s[end] in visited:
      start = max( start, visited[s[end]] + 1)
    visited[s[end]] = end
    maxleng = max( maxleng, end-start + 1)
            
  return maxleng
