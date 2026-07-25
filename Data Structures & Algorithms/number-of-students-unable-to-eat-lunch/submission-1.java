class Solution {
    public int countStudents(int[] students, int[] sandwiches) {
        int square=0, circle=0;
        for(int i : students){
            if(i==0) circle+=1;
            else square+=1;
        }

        for(int sandwich : sandwiches){
            if(sandwich==0 && circle>0) circle-=1;
            else if(sandwich==1 && square>0) square-=1;
            else return circle+square;
        }
        return 0;
    }
}