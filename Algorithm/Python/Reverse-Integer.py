
def reverse(x):
        """
        :type x: int
        :rtype: int
        """
        str_x = str(x)
        if x<0:
            str_x = '-'+str_x[::-1][:-1]
            x = int(str_x)
        else:
            str_x = str_x[::-1]
            x = int(str_x)
        neg_limit= -0x80000000
        pos_limit= 0x7fffffff
        
        if(x<0):
            val=x&neg_limit
            if(val==neg_limit):
                return x
            else:
                return 0
        elif(x==0):
            return x
        else:
            val = x&pos_limit
            if(val==x):
                return x
            else:
                return 0
              
if __name__ == '__main__':
    x = 123
    print(reverse(x))
