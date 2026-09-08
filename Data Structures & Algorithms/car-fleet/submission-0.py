class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #brute force
        # change the position of all cars by their speed
        # check  all cars to see if any have the same position 
        # if they do increment fleet count and add pair to set 
        # if already in set, don't count 

        # [0, 3, 5, 8, 10]
        pair = [[p, s] for p,s in zip(position, speed)]
        stack = []
        for p,s in sorted(pair)[::-1]:
            stack.append((target - p) / s)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
