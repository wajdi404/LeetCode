import time


def isValid(s):
    """
    :type s: str
    :rtype: bool
    """
    if (s.count('(') != s.count(')')) or (s.count('[') != s.count(']')) or (s.count('{') != s.count('}')):
        return False

    stack = []
    for i in range(len(s)):
        if s[i] in '({[':
            stack.append(s[i])
        elif len(stack):
            c = stack.pop()
            if (c == '(' and s[i] in '}]') or (c == '[' and s[i] in '})') or (c == '{' and s[i] in '])'):
                return False
    return True


if __name__ == '__main__':
    # s = "()"
    s = "()()[]{}{}{}[[][]]"
    # s = "(]"
    # s = "([)]" # False
    t0 = time.time()
    print(isValid(s))
    t1 = time.time()
    print(t1 - t0)
