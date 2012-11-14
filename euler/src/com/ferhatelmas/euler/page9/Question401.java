package com.ferhatelmas.euler.page9;

import java.math.BigInteger;

public class Question401 {
  static long max = (long)Math.pow(10, 15);
  static BigInteger two = new BigInteger("2"), six = new BigInteger("6");

  public static void main(String[] args) {
    BigInteger sum = BigInteger.ZERO;
    long diff, div;
    for(long i=1; i<=max; i=1+Math.max(diff, i)) {
      div = max / i;
      diff = max / div;
      sum = sum.add(getSquareSum(div).multiply(new BigInteger(String.valueOf(diff-i+1))));
    }

    String s = sum.toString();
    System.out.println(s.substring(s.length()-9));
  }

  private static BigInteger getSquareSum(long n) {
    BigInteger b = new BigInteger(String.valueOf(n));
    b = b.multiply(b.add(BigInteger.ONE).multiply(b
        .multiply(two).add(BigInteger.ONE)))
        .divide(six);
    return b;
  }
}
