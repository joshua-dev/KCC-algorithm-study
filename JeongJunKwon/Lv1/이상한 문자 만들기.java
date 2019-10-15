class Solution {
  public String solution(String s) {
      String answer = "";
      int count = 0;
      for(int i = 0; i < s.length(); i++) {
          String a = s.substring(i, i+1);
          if(a.equals(" ")) {
              count = 0;
              answer = answer + " ";
              continue;
          }
          
          if(count % 2 == 0) {
             answer = answer + a.toUpperCase();
          } else {
              answer = answer + a.toLowerCase();
          }
          count++;
      }
      return answer;
  }
}