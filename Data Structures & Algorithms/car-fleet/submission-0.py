class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars=[(position[i], speed[i]) for i in range(len(position))]
        stack=[]
        for pair in sorted(cars)[::-1]:
            print(pair[0], pair[1])
            stack.append((target-pair[0])/pair[1])
            # if the car behind crashes, remove it from stack
            if len(stack)>=2 and stack[-1]<=stack[-2]:
                stack.pop()

        
        return len(stack)