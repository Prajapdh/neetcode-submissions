class Solution {
    public int[] getFinalState(int[] nums, int k, int multiplier) {
        PriorityQueue<int[]> minHeap = new PriorityQueue<>((a, b) -> {
            if (a[0] != b[0]) return Integer.compare(a[0], b[0]);
            return Integer.compare(a[1], b[1]);
        });

        for (int i = 0; i < nums.length; i++) {
            minHeap.offer(new int[]{nums[i], i});
        }

        for (int i = 0; i < k; i++) {
            int[] pair = minHeap.poll();
            pair[0] *= multiplier;
            nums[pair[1]] = pair[0];
            minHeap.offer(pair);
        }

        return nums;
    }
}