package com.ferhatelmas.eolimp.page1.q9;

import java.util.Scanner;

public class Main {

  private static int min = Integer.MAX_VALUE;
  private static int cnt = 0;
  private static int digitCnt;

  public static void main(String[] args) {
    digitCnt = new Scanner(System.in).nextInt();

    if(digitCnt == 0) {
      System.out.println(1 + " " + 0);
      return;
    } else if(digitCnt == 1) {
      System.out.println(10 + " " + 0);
      return;
    }

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<digitCnt-2; i++)
      sb.append(1);
    sb.append(2);
    sb.append(digitCnt);
    int m = Integer.parseInt(sb.toString());

    int cnt = digitCnt*(digitCnt-1);
    if(digitCnt == 2) cnt /= 2;
    else if(digitCnt == 5 || digitCnt == 7 || digitCnt == 9) cnt *= 2;
    else if(digitCnt == 8) cnt *= 4;
    System.out.println(cnt + " " + m);

    //generate(0, new int[digitCnt]);
    //System.out.println(cnt + " " + min);
  }

  // to actually generate numbers and see the pattern
  private static void generate(int n, int[] number) {
    if(n >= digitCnt) {
      if(isNDigit(number.length-1, number)) {
        int v = getNumber(number.length-1, number);
        System.out.println(v);
        min = Math.min(min, v);
        cnt++;
      }
      return;
    }

    for(int i=n==0&&digitCnt!=1?1:0; i < 10; i++) {
      number[n] = i;
      generate(n+1, number);
    }
  }

  private static int getNumber(int offset, int[] digits) {
    char[] chars = new char[offset+1];
    for(int i=0; i<chars.length; i++)
      chars[i] = (char)((int)'0' + digits[i]);
    return Integer.parseInt(new String(chars));
  }

  private static boolean isNDigit(int offset, int[] n) {
    int sum = 0, product = 1;
    for(int i=0; i<=offset; i++) {
      sum += n[i];
      product *= n[i];
    }
    return sum == product;
  }
}
