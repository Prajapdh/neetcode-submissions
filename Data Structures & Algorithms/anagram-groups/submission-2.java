class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String,List<String>> anagrams = new HashMap<>();

        for(String word : strs){
            int[] counter = new int[26];
            for(char c : word.toCharArray()){
                counter[c-'a']++;
            }
            String key = Arrays.toString(counter);
            anagrams.putIfAbsent(key, new ArrayList<>());
            anagrams.get(key).add(word);
        }
        return new ArrayList<>(anagrams.values());
    }
}
