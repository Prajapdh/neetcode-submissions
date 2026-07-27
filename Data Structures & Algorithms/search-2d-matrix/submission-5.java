class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int ROWS = matrix.length, COLS = matrix[0].length;

        int l = 0, r = ROWS - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (matrix[mid][0] == target) return true;
            if (matrix[mid][0] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        int searchRow = r;
        if (searchRow < 0) return false;
        if (target > matrix[searchRow][COLS - 1]) return false;

        l = 0;
        r = COLS - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (matrix[searchRow][mid] == target) return true;
            if (matrix[searchRow][mid] < target) {
                l = mid + 1;
            } else {
                r = mid - 1;
            }
        }

        return false;
    }
}