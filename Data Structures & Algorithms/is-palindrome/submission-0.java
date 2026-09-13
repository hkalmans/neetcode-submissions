class Solution {
    public boolean isPalindrome(String s) {
        StringBuilder test = new StringBuilder();
        for(char c : s.toCharArray()){
            if(Character.isLetterOrDigit(c)) {
                test.append(Character.toLowerCase(c));
            }
        }
        return test.toString().equals(test.reverse().toString());
    }
}
