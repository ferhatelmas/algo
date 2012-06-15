package com.ferhatelmas.euler.page8;

public class Question383 {

  public static void main(String[] args) {

    System.out.println(t(18));

  }

  private static long t(int power) {

    // values come from --> tBrute((long)(Math.pow(2, 18) * Math.pow(5, power)));
    if(power == 6) return 7812294;
    if(power == 7) return 26948412;

    return 5*t(power-2) + 2*t(power-1);
  }

  private static long f(long n) {
    long cnt = 0;
    while(n >= 5) {
      n /= 5;
      cnt += n;
    }

    return cnt;
  }

  private static long tBrute(long n) {

    long cnt = 0;

    for(long i=1; i<=n; i++) {
      if(f(2*i-1) < 2*f(i)) cnt++;
    }

    return cnt;
  }

}
