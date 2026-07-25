class Solution {
    public int[] intersection(int[] nums1, int[] nums2) {
        HashSet<Integer> numSet= new HashSet<>();
        for(int n : nums1){
            numSet.add(n);
        }

        ArrayList<Integer> res = new ArrayList<>();
        for(int n : nums2){
            if(numSet.contains(n)){
                res.add(n);
                numSet.remove(n);
            }
        }
        return res.stream().mapToInt(Integer::intValue).toArray();
    }
}