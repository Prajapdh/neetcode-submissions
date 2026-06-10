class CountSquares {
    private Map<List<Integer>, Integer> ptsMap;

    public CountSquares() {
        ptsMap = new HashMap<>();
    }

    public void add(int[] point) {
        List<Integer> key = Arrays.asList(point[0], point[1]);
        ptsMap.put(key, ptsMap.getOrDefault(key, 0) + 1);
    }

    public int count(int[] point) {
        int x = point[0], y = point[1];
        int res = 0;

        for (List<Integer> p : ptsMap.keySet()) {
            int px = p.get(0), py = p.get(1);
            // Check diagonal: same Manhattan distance in x and y (square diagonal)
            if (Math.abs(px - x) == Math.abs(py - y) && px != x && py != y) {
                List<Integer> corner1 = Arrays.asList(px, y);
                List<Integer> corner2 = Arrays.asList(x, py);
                if (ptsMap.containsKey(corner1) && ptsMap.containsKey(corner2)) {
                    res += ptsMap.get(p) * ptsMap.get(corner1) * ptsMap.get(corner2);
                }
            }
        }
        return res;
    }
}   