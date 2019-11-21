class Solution {
  public int solution(int n) {
      int answer = 0;
      if(n == 1) return 1;
      else if (n == 2) return 2;
      long n1 = 1;
      long n2 = 2;
      long n3 = n1 + n2;
      for(int i = 3; i <= n; i++) {
          n3 = (n1 + n2) % 1000000007;
          n1 = n2;
          n2 = n3;
      }
      
      answer = (int) n3;
      return answer;
  }
}