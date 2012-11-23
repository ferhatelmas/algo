package com.ferhatelmas.poj.vol12.p2196;

public class Main {

  public static void main(String[] args) {
    for(int i=2992; i<10000; i++) {
      if(isThreeSum(i)) System.out.println(i);
    }
  }

  private static boolean isThreeSum(int i) {
    int sum = getSum(i, 10);
    return sum == getSum(i, 16) && sum == getSum(i, 12);
  }

  private static int getSum(int n, int b) {
    int sum = 0;
    for(char c : Integer.toString(n, b).toCharArray())
      sum += c - (c >= 'a' ? 'a'-10 : '0');
    return sum;
  }
}
