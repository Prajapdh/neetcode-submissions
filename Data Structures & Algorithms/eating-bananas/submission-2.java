class Solution {
    public int minEatingSpeed(int[] piles, int h) {
        //  h= time to eat all bananas
        // min speed to eat all bananas within h hours
        int l=0;
        int r=Arrays.stream(piles).max().getAsInt();
        int res=r;
        while(l<=r){
            int mid = (r-l)/2+l;
            long timeTaken=0;
            for(int pile : piles){
                timeTaken+=Math.ceil((double)pile/mid);
            }
            if(timeTaken<=h){
                res=mid;
                r=mid-1;
            }else{
                l=mid+1;
            }
        }

        return res;
    }
}
