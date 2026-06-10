class Solution {
    public int minSubArrayLen(int target, int[] nums) {
        int n = nums.length;
        int[] prefixSum = new int[n+1];
        prefixSum[0]=0;
        for(int i=0; i<n; i++){
            prefixSum[i+1]=prefixSum[i]+nums[i];
            // System.out.print(prefixSum[i+1]+ " ");
        }
        int res=n+1;
        for(int i=0; i<n; i++){
            int l=i, r=n;   //r=n is in range of prefixSum list
            while(l<r){
                int mid = (r-l)/2+l;
                int curSum = prefixSum[mid+1]-prefixSum[i];
                if(curSum>=target) r=mid;
                else l=mid+1;
            }
            // if size of window is 0
            if(l!=n) res=Math.min(res, l-i+1);
        }
        return res%(n+1);
    }
}