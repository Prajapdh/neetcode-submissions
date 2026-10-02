from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        counts = [0] * (max(people) + 1)

        for weight in people:
            counts[weight] += 1

        left = 0
        right = len(counts) - 1
        remaining = len(people)
        boats = 0

        while remaining > 0:
            # Find the heaviest remaining person.
            while counts[right] == 0:
                right -= 1

            # Every round, the heaviest person uses one boat.
            counts[right] -= 1
            remaining -= 1
            boats += 1

            # Find the lightest remaining person.
            while left <= right and counts[left] == 0:
                left += 1

            # Pair with at most one lightest person.
            if remaining > 0 and left <= right and left + right <= limit:
                counts[left] -= 1
                remaining -= 1

        return boats