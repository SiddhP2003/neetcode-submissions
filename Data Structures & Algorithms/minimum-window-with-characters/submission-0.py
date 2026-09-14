class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #brute force 
        #check every substring from length t to length s and the first occurance of all characters return that substring 
        # O(m^2n)

        #optimal solution
        # sliding window that checks to see length from t to length to s and checks if count of characters is the same as t 
        # O(n)
        if t == "":
            return ""

        countT, window = {}, {}
        for c in t:
            countT[c] = countT.get(c, 0) + 1
        
        have, need = 0, len(countT)
        res, resLen = [-1, -1], float("infinity")
        l = 0
        for r in range(len(s)):
            c = s[r]
            window[c] = 1 + window.get(c, 0)

            if c in countT and window[c] == countT[c]:
                have += 1
            
            while have == need:
                if (r - l + 1) < resLen:
                    res = [l, r]
                    resLen = (r - l + 1)
                window[s[l]] -= 1
                if s[l] in countT and window[s[l]] < countT[s[l]]:
                    have-=1
                l += 1
        l,r = res

        return s[l:r+1] if resLen != float("infinity") else ""
