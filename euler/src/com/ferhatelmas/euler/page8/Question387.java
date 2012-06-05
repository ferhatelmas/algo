package com.ferhatelmas.euler.page8;

import java.math.BigInteger;

public class Question387 {

  private static long sum = 0;

  public static void main(String[] args) {
    yield(new StringBuilder());
    System.out.println(sum);
  }

  private static void yield(StringBuilder sb) {

    if(sb.length() >= 14) return;

    for(int i= sb.length()>0 ? 0 : 1; i<10; i++) {
      sb.append(i);
      long num = Long.parseLong(sb.toString());
      if(isRightTruncatable(num)) {
        if(new BigInteger(sb.toString()).isProbablePrime(60) && isStrong(num/10)) {
          sum += num;
        }
        yield(sb);
      }
      sb.deleteCharAt(sb.length()-1);
    }
  }

  private static boolean isStrong(long n) {
    int val = getSum(n);
    return val != 0 && BigInteger.valueOf(n/getSum(n)).isProbablePrime(60);
  }

  private static int getSum(long n) {
    String s = String.valueOf(n);
    int den = 0, len = s.length();
    for(int i=0; i<len; i++) {
      den += (s.charAt(i) - '0');
    }
    return den;
  }

  private static boolean isRightTruncatable(long n) {

    long tmp = n;
    while((tmp/=10) > 0 && tmp%getSum(tmp) == 0);

    return tmp==0;
  }

}
