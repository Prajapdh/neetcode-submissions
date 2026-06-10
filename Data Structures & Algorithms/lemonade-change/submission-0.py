class Solution:
    def lemonadeChange(self, bills: List[int]) -> bool:
        register={5:0, 10:0, 20:0}

        for bill in bills:
            change=bill-5
            if change<0:
                return False
            else:
                while change:
                    print(bill, change, register)
                    if change>=20 and register[20]>0:
                        change-=20
                        register[20]-=1
                    elif change>=10 and register[10]>0:
                        change-=10
                        register[10]-=1
                    elif change>=5 and register[5]>0:
                        change-=5
                        register[5]-=1
                    else:
                        return False
            register[bill]+=1
        return True

