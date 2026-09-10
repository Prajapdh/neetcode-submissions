class Solution {
    public int[] twoSum(int[] nums, int target) {
        int[][] numbers = new int[nums.length][2];
        for(int i=0; i<nums.length; i++){
            numbers[i][0]=nums[i];
            numbers[i][1]=i;
        }
        Arrays.sort(numbers, Comparator.comparingInt(a->a[0]));
        int l=0, r=nums.length-1;

        while(l<r){
            int sum = numbers[l][0]+numbers[r][0];
            if(sum==target){return new int[] {Math.min(numbers[l][1], numbers[r][1]),Math.max(numbers[l][1], numbers[r][1])};}
            else if(sum>target){r-=1;}
            else{l+=1;}
        }
        return new int[] {Math.min(numbers[l][1], numbers[r][1]),Math.max(numbers[l][1], numbers[r][1])};
    }
}
