class Solution {
    public int solution(String name) {
		int answer = 0;
		int[] count = {0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,7,6,5,4,3,2,1};
        int[] nameCount = new int[name.length()];
        
        for(int i = 0; i < name.length(); i++) {
            char c = name.charAt(i);
            nameCount[i] = count[c - 'A'];
        }
        
        int leftCount = 1;
        int rightCount = 1;
        int cursor = 0;
        int left = nameCount.length - 1;
        int right = 1;
        
        while(true) {
            if(nameCount[cursor] != 0) {
                answer += nameCount[cursor];
                nameCount[cursor] = 0;
            }

            System.out.printf("left: %d, right: %d, cursor: %d", left, right, cursor);
        	System.out.printf(", nameCount[%d]: %d", cursor, nameCount[cursor]);
            
            while(nameCount[left] == 0 && left != cursor) {
                leftCount++;
                left = left == 0 ? nameCount.length - 1 : left - 1;
            }
            
            while(nameCount[right] == 0 && right != cursor) {
                rightCount++;
                right = (right + 1) % nameCount.length;
            }
            if(left == cursor || right == cursor) break;
            if(leftCount >= rightCount) {
                answer += rightCount;
                cursor = right;
            } else {
                answer += leftCount;
                cursor = left;
            }

            left = cursor == 0 ? nameCount.length - 1 : cursor - 1;
            right = (cursor + 1) % nameCount.length;
            
            leftCount = 1; rightCount = 1;
            System.out.printf("\n");
        }
		return answer;
    }
}