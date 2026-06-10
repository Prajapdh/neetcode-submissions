class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # Build (position, time) pairs
        cars = [(p, (target - p) / s) for p, s in zip(position, speed)]
        
        # Sort by starting position descending (from closest to target to farthest)
        cars.sort()
        
        stack = []  # will store times of fleets
        for pos, t in cars:
            # If current car takes longer than the fleet ahead, it forms a new fleet
            # If it is faster (t <= stack[-1]), it joins that fleet, so we do nothing
            while stack and stack[-1]<=t:
                stack.pop()
            stack.append(t)
        
        return len(stack)
