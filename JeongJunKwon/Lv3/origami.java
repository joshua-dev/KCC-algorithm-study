import java.util.List;
import java.util.ArrayList;
import java.util.Arrays;

class Solution {
  public int[] solution(int n) {
      List<Integer> list = new ArrayList<>();
      while(n > 0) {
          if(list.isEmpty()) {
              list.add(0);
          } else {
              List<Integer> before = new ArrayList<>();
              List<Integer> after = new ArrayList<>();
              before = list;
              for(int i = list.size() - 1; i >= 0; i--) {
                  int value = list.get(i);
                  value = value == 1 ? 0 : 1;
                  after.add(value);
              }
              before.add(0); before.addAll(after);
              list = before;
          }
          n--;
      }
      
      int[] answer = new int[list.size()];
      for(int i = 0; i < list.size(); i++) {
          answer[i] = list.get(i);
      }
      return answer;
  }
}