class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        cars = []
        for p,s in zip(position, speed):
            cars.append((p,s))
        cars.sort(reverse=True)
        print(cars)
        stack=[]   #stores time taken by last fleet
        for p,s in cars:
            time = (target-p)/s
            if stack and time<=stack[-1]:
                print(f"prev time: {stack[-1]}, time: {time}")
                continue
            stack.append(time)
        
        return len(stack)