class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # return no of students unable to eat
        # reasons: if not enough sandwiches, 
        demand = [0,0]
        for s in students:
            demand[s]+=1
        for s in sandwiches:
            if demand[s]>0:
                demand[s]-=1
            else:
                break
        return demand[0]+demand[1]