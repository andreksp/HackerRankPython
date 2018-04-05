
import sys

class BalancedBrakets(object):
    """Two brackets are considered to be a matched pair if the an opening bracket (i.e., (, [, or {) occurs to the left 
    of a closing bracket (i.e., ), ], or }) of the exact same type. There are three types of matched pairs of brackets: 
    [], {}, and ().
    
    """

    def __init__(self):
        pass

    def is_matched(self, expression):

        temp = expression

        newstr = expression.replace("[]", "").replace("{}", "").replace("()", "");

        if newstr == "":
            return True

        if newstr != temp:
            return is_matched(self, newstr);

        return False
            

    def process(self):
        t = int(input().strip())
        for a0 in range(t):
            expression = input().strip()
            if is_matched(expression) == True:
                print("YES")
            else:
                print("NO")


