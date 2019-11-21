import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = people.length;
        
        Arrays.sort(people);
        
        int sum = 0;
        int count = 0;
        int startIndex = 0;
        
        for(int endIndex = people.length - 1; endIndex >= 0; endIndex--) {
            if(startIndex == endIndex) break;
            
            if(people[startIndex] + people[endIndex] <= limit) {
                answer--;
                startIndex++;
            }
            
            if(startIndex == endIndex) break;
        }
        
        return answer;
    }
}