class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #brute force 
        # start from each temperature and interate until you find a higher temeperatue and store number of iterations 
        # O(n^2)

        res = [0] * len(temperatures)
        stack = []

        for i, t in enumerate(temperatures):
            while stack and t > temperatures[stack[-1]]:
                stackI = stack.pop()
                res[stackI] = (i - stackI)
            stack.append(i)
        
        return res
        
