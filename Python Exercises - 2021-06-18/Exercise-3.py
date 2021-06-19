""" 
Program to Print all Prime Numbers in an Interval of 5 seconds
"""

import time


class Solution(object):
    def prime(self):
        print("Starting to Print all Prime Number for 5 second")
        time.sleep(1)
        starttime = time.time()
        num = 3
        while True:
            for i in range(2, num):
                if num % i == 0:
                    break
                else:
                    print(num)
                    break
            num += 1
            if (time.time() - starttime) > 5 :
                print("Time Limit Exceeded.........")
                return
            

Solution().prime()
