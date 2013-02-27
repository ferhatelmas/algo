package com.ferhatelmas.euler.page3;

import java.math.BigInteger;

public class Question113 {

  public static void main(String[] args) {
    System.out.println(comb(109, 9) + comb(110, 10) - 1002);
  }

  private static long comb(int n, int k) {
    BigInteger mul = BigInteger.ONE;
    for(int i=0; i<k; i++)
      mul = mul.multiply(new BigInteger(String.valueOf(n - i)));
    for(int i=2; i<=k; i++)
      mul = mul.divide(new BigInteger(String.valueOf(i)));
    return mul.longValue();
  }

}
