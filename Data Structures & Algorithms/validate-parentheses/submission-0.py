class Solution:
    def isValid(self, s: str) -> bool:
        # stack 
        # having stack hold open parantheses and removing on closed parentheses 
        # if close and open do not match return false 
        # if stack is empty at the end return true 
        # O(n) Space O(n)
        stk = []
        brackets = {
            ')':'(',
            ']':'[',
            '}':'{'
        }

        for i in range(len(s)):
            if len(stk) == 0:
                stk.append(s[i])
            elif s[i] in ['(', '{', '[']:
                stk.append(s[i])
            elif s[i] not in ['(', '{', '[']:
                if stk[-1] == brackets[s[i]]:
                    stk.pop()
                else:
                    return False

        if len(stk) == 0:
            return True
        else:
            return False
            
