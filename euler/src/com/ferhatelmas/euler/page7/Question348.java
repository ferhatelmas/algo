package com.ferhatelmas.euler.page7;

public class Question348 {

  public static void main(String[] args) {

    int sum = 0;
    int lim, count = 0, len = 7;
    while(true) {

      lim = (int)Math.pow(10, len / 2 + (len % 2));

      for(int i=lim/10; i<lim; i++) {
        int palindrome = Integer.parseInt(String.valueOf(i) +
            new StringBuilder().append(i).reverse().substring(len%2 == 0 ? 0 : 1));

        if(isWanted(palindrome)) {
          System.out.println(palindrome);
          sum += palindrome;
          if(++count == 5) {
            System.out.println(sum);
            System.exit(0);
          }
        }
      }
      len++;
    }
  }

  private static boolean isWanted(int l) {

    int cnt = 0, limit = (int)Math.cbrt(l-4);
    for(int i=2; i<=limit; i++) {
      double root = Math.sqrt(l-i*i*i);
      if(root - (int)root == 0) {
        cnt++;
      }
    }

    return cnt == 4;
  }

}
