class Solution:

    def encode(self, strs: List[str]) -> str:
        # take in input strings 
        # convert values into 
        # encode each world you can use by multiplying the int value of each char by 2 
        # encode seperation between words with *&*
        res = ""

        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        #take the encoded string 
        res = []
        i = 0
        while i < len(s):
            j = i 
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j + 1 : j + 1 + length])
            i = j + 1 + length
        return res