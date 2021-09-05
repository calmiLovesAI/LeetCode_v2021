

# The rand7() API is already defined for you.
# def rand7():
# @return a random integer in the range 1 to 7


# randX()*Y + randY()   生成1~XY之间的随机数

import random

def rand7():
    return random.randint(1, 7)



class Solution:
    def rand10(self):
        """
        :rtype: int
        """
        while True:
            ans = (rand7() - 1) * 7 + rand7()
            if ans <= 40:
                return (ans % 10) + 1
            ans = (ans - 40 - 1) * 7 + rand7()
            if ans <= 60:
                return (ans % 10) + 1
            ans = (ans - 60 - 1) * 7 + rand7()
            if ans <= 20:
                return (ans % 10) + 1

