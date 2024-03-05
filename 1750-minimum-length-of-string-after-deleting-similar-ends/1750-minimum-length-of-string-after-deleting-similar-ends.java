class Solution {
    public int minimumLength(String s) {
        int i=0;
        int j=s.length()-1;
        while(i<j){
            if (s.charAt(i)==s.charAt(j)){
                while(i+1<j && s.charAt(i)==s.charAt(i+1)) i++;
                while(i<j-1 && s.charAt(j)==s.charAt(j-1)) j--;
            }
            else return j-i+1;
            i+=1;
            j-=1;
        }
        return j-i+1;
    }
}