import java.util.*;

class Solution {
    public int solution(String arrangement) {
        int answer = 0;
        Queue<String>  par = new LinkedList<>();
        boolean isLaser = false;
        
        for(int i = 0; i < arrangement.length(); i++) {
            par.add(arrangement.substring(i, i + 1));
        }
        
        int count = 0;
        while(!par.isEmpty()) {
            String a = par.poll();
            
            if(a.equals("(")) {
                if(!isLaser) {
                    isLaser = true;
                } else {
                    count++;
                }
            } else if (a.equals(")")) {
                if(isLaser) {
                    answer += count;
                    isLaser = false;
                } else {
                    answer += 1;
                    count -= 1;
                }
            }
        }
        return answer;
    }
}