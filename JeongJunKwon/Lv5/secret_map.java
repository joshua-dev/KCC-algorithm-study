class Solution {
  public String[] solution(int n, int[] arr1, int[] arr2) {
      String[] answer = new String[n];
      
      for(int i = 0; i < n; i++) {
          String bin1 = binary(n, arr1[i]);
          String bin2 = binary(n, arr2[i]);
          
          String total = "";
          for(int j = 0; j < n; j++) {
              if(bin1.substring(j, j + 1).equals("1") || bin2.substring(j, j + 1).equals("1")) {
                  total =  total + "#";
              } else {
                  total = total + " ";
              }
          }
          
          answer[i] = total;
      }
      return answer;
  }

    public String binary(int n, int num1) {
        String bin1 = "";
        
        while(num1 > 0) {
            int a = num1 % 2;
            bin1 = Integer.toString(a) + bin1;
            num1 /= 2;
        }
        
        while(bin1.length() != n) {
            bin1 = "0" + bin1;
        }
        return bin1;
    }
}