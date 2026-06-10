class Solution:
    def checkValidString(self, s: str) -> bool:
        # lets save a range
        minn, maxx = 0,0
        for c in s:
            # Add 1 for every opening para
            if(c=="("):
                minn+=1
                maxx+=1
            # Decrease 1 for every closing para
            elif(c==")"):
                minn=minn-1
                maxx=maxx-1
            else:
                minn=minn-1
                maxx=maxx+1
            # negative values are not possible, so we wont consider those
            if minn<0: minn=0
            if maxx<0: return False
        
        return True if (minn==0) else False