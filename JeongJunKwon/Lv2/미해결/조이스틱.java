public class Solution {
	public int solution(String name) {
		int answer = 0;
		int[] count = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1};
        int[] nameCount = new int[name.length()];
        int length = 0;
        
        for(int i = 0; i < name.length(); i++) {
            char c = name.charAt(i);
            nameCount[i] = count[c - 'A'];
            if(nameCount[i] != 0) length++;
        }
        if(nameCount[0] == 0) length++;
        
        int leftCount = 1;
        int rightCount = 1;
        int cursor = 0;
        
        while(length > 0) {
            if(nameCount[cursor] != 0) {
                answer += nameCount[cursor];
                nameCount[cursor] = 0;
            }
            System.out.printf("%d\t", answer);
            
            int left = cursor == 0 ? name.length() - 1 : cursor - 1;
        	int right = (cursor + 1) % name.length();
        	
            while(nameCount[left] == 0 && left == cursor) {
//            	System.out.println(nameCount[left]);
                leftCount++;
                left = left == 0 ? nameCount.length - 1 : left - 1;
            }
            
            while(nameCount[right] == 0 && right == cursor) {
//            	System.out.println(nameCount[right]);
                rightCount++;
                right = (right + 1) % nameCount.length;
            }
//            System.out.println(rightCount + ", " + leftCount);
            
            if(leftCount >= rightCount) {
                answer += rightCount;
                cursor = right;
            } else {
                answer += leftCount;
                cursor = left;
            }
            leftCount = 1; rightCount = 1;
            length--;
        }
		return answer;
	}
}
