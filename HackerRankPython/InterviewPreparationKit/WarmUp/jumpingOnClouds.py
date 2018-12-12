

import sys

class JumpingOnClouds():    
    def __init__(self):
        pass

    def processJumpingOnClouds(self, c):
        total = 0
        i = 0
        while  i < len(c):
            if (c[i] == 1):
                i += 1
                continue
    
            if (i + 2 < len(c) and c[i] == c[i + 1] and c[i] == c[i + 2]):
                i += 1

            total += 1
            
            i += 1

        return total - 1

    def process(self):
        n = input().strip()
        n = [int(n)]
        ar = list(map(int, input().strip().split(' ')))
        result = self.processJumpingOnClouds(ar)
        print(result)


    def __del__(self):
        pass
