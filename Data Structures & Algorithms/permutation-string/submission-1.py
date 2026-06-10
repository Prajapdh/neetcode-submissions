class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        m1={}
        for c in s1:
            if c not in m1:
                m1[c]=1
            else:
                m1[c]+=1
        
        left,right=0,0
        m2={}
        while(right<len(s2)):
            if s2[right] not in m2:
                m2[s2[right]]=1
            else:
                m2[s2[right]]+=1
            right+=1

            if(right-left==len(s1)):
                # print(m1, m2)
                if m1 == m2:
                    return True
                # print(f"removing: {s2[left]} from map")
                m2[s2[left]]-=1
                if m2[s2[left]]==0:
                    del m2[s2[left]]
                # print(m2)
                left+=1
            
            
            
            # print(f"l: {left}, r: {right}")
        return False