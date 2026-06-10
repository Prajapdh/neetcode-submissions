class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # count={}
        # freq=[[] for i in range(len(nums)+1)] #[0,1,2,3,4,...]

        # for n in nums:
        #     count[n] = 1 + count.get(n,0)
        
        # for n,c in count.items():
        #     freq[c].append(n);
        # ans=[]
        # for i in range(len(freq)-1,0, -1):
        #     for n in freq[i]:
        #         ans.append(n)
        #         if len(ans)==k:
        #             return ans
        count={}
        for n in nums:
            count[n]=1+count.get(n,0)

        sorted_items = sorted(count.items(), key=lambda x: x[1], reverse=True)   #sorting using x[0] as value, here x=[count, number]
        print(sorted_items)
        result = [item[0] for item in sorted_items[:k]]
        return result
                