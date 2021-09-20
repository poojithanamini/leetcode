class Solution:
    def __init__(self):
        self.left = ['[','(','{']
        self.right = [']',')','}']
        self.both = ['[]','()','{}']
    def isValid(self, s: str) -> bool:
        stack = []
        for i in s:
            if i in self.left:
                stack.append(i)
            else:
                if(stack==[]):
                    return False
                if (str(stack[-1])+str(i) in self.both):
                    stack.pop()
                else:
                    return False
        
        return True if (stack==[]) else False