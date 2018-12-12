

import sys
#from collections import Counter

class SockMerchant():    
    def __init__(self):
        pass

    def processSockMerchant(self, n, ar):  

        grouped = dict()
        for item in ar:
            if not item in grouped:
                grouped[item] = 0

            grouped[item] += 1

        #grouped = Counter(ar)

        totalPairs = 0

        for g in grouped:
            totalPairs += grouped[g] // 2

        return totalPairs;

    def process(self):
        n = input().strip()
        n = [int(n)]
        ar = list(map(int, input().strip().split(' ')))
        result = self.processSockMerchant(n, ar)
        print(result)


    def __del__(self):
        pass
