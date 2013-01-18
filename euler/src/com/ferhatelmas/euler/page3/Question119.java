package com.ferhatelmas.euler.page3;

public class Question119 {

  public static void main(String[] args) {
    int cnt = 0;
    for(long i=2; i < 100; i++)
      for(int j=2; j < 20; j++) {
        long l = (long)Math.pow(i, j);
        if(getDigitSum(l) == i)
          if(++cnt == 30) {
            System.out.println(l);
            return;
          }
      }
  }

  private static int getDigitSum(long n) {
    int sum = 0;
    for(char c : String.valueOf(n).toCharArray())
      sum += c - '0';
    return sum;
  }
}
