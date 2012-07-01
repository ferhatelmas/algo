package com.ferhatelmas.euler.page3;

import java.util.Arrays;

public class Question127 {

  private static int[] rads = new int[120000];

  public static void main(String[] args) {

    Arrays.fill(rads, 1);
    for(int i=2; i<rads.length; i++) {
      if(rads[i] == 1) {
        for(int j=i; j<rads.length; j+=i) {
          rads[j] *= i;
        }
      }
    }

    int k, sum = 0, inc;
    for(int i=1; i<60000; i++) {
      inc = 2 - i%2;
      for(int j=i+1; j<120000; j+=inc) {
        k = i + j;
        if(k >= 120000) break;
        if((long)rads[i]*rads[j]*rads[k] < k &&
            gcd(rads[i], rads[j]) == 1) {
          sum += k;
        }
      }
    }

    System.out.println(sum);
  }

  private static int gcd(int a, int b) {

    int tmp;
    while(b != 0) {
      tmp = b;
      b = a%b;
      a = tmp;
    }

    return a;
  }
}
