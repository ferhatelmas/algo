package com.ferhatelmas.eolimp.page1.q29;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    BigInteger b = new BigInteger(new Scanner(System.in).nextLine().trim());
    int cnt = 0;
    while(!isPalindrome(b)) {
      cnt++;
      b = next(b);
    }
    System.out.println(cnt);
  }

  private static boolean isPalindrome(BigInteger b) {
    String s = b.toString();
    return s.equals(new StringBuilder(s).reverse().toString());
  }

  private static BigInteger next(BigInteger b) {
    return b.add(new BigInteger(new StringBuilder(b.toString()).reverse().toString()));
  }
}
