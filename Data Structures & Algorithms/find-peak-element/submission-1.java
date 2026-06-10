class Solution {
    public int findPeakElement(int[] nums) {
        // We need to search in the side where a peak element is guaranteed
        // if a neighbor element is greater than mid value, than that side should have a solution
        int n = nums.length;
        int l= 0; 
        int r= n-1;
        while(l<r){
            int mid = (r-l)/2+l;
            if(mid+1<n && nums[mid+1]>nums[mid]){
                l=mid+1;
            }
            else if(mid>0 && nums[mid-1]>nums[mid]){
                r=mid-1;
            }
            else return mid;
        }
        return l;
    }
}