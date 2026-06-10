class Solution {
    public int firstMissingPositive(int[] nums) {
        // Convert all negative values to 0
        for(int i=0; i<nums.length; i++){
            if(nums[i]<0) nums[i]=0;
        }
        // Mark elements at (element-1)index as negative, if found in the array
        // Our solution set is from [1, len(nums)], max solution is len(nums)
        // if 0 is encountered, replace it with -len(nums)
        int n = nums.length;
        for(int i=0; i<n; i++){
            int ele = Math.abs(nums[i]);
            if(ele-1>=0 && ele-1<n){
                if(nums[ele-1]==0) nums[ele-1]=-1*n;
                else if(nums[ele-1]>0) nums[ele-1]*=-1;
            }
        }
        // for(int num: nums){System.out.print(String.valueOf(num) + " ");}
        for(int i=1; i<=n; i++){
            if(nums[i-1]>=0) return i;
        }
        return n+1;
    }
}