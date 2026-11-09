class Solution:
    def romanToInt(self, s: str) -> int:
        #loop through string and add roman numerals 
        #if roman numberal after a certain character is greater, add negative amount of current character
        # use map to map values 
        map = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }
        res = 0 

        for i in range(len(s)):
            if i + 1 < len(s) and map.get(s[i + 1]) > map.get(s[i]):
                res += (-1 * map.get(s[i]))
            else:
                res += map.get(s[i])
        
        return res
            