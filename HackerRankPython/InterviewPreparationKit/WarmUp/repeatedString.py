

import sys

class RepeatedString():    
    def __init__(self):
        pass

    def processRepeadString(self, s, n):
        totalNumberOfAs = int(n / len(s)) * s.count('a')

        missingChars = int(n % len(s));

        if (missingChars > 0):
            totalNumberOfAs += s[:missingChars].count('a')
            
        return totalNumberOfAs

    def process(self):
        s = input()
        n = input().strip()
        n = int(n)
        
        result = self.processRepeadString(s, n)
        print(result)


    def __del__(self):
        pass
