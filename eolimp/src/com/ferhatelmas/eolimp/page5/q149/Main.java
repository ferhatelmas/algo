package com.ferhatelmas.eolimp.page5.q149;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(n < 200 ? getDigitCountSlowly(n) : getDigitCount(n));
  }

  private static int getDigitCount(int n) {
    int d1 = (int)Math.floor(1 + Math.log10(Math.sqrt(2 * Math.PI * n)) + n * Math.log10(n / Math.E)),
        d2 = (int)Math.floor(d1 + Math.log10(Math.E / Math.sqrt(2 * Math.PI)));
    assert d1 == d2;
    return d1;
  }

  private static int getDigitCountSlowly(int n) {
    BigInteger b = BigInteger.ONE;
    for(int i=2; i<=n; i++) b = b.multiply(new BigInteger(String.valueOf(i)));
    return b.toString().length();
  }
}
