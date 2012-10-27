package com.ferhatelmas.eolimp.page40.q1205;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    BigInteger b = new BigInteger(in.next());
    System.out.println(invPow(b, n));

  }

  private static BigInteger invPow(BigInteger b, int n) {
    BigInteger high = BigInteger.ONE, low, mid = BigInteger.ZERO, two = new BigInteger("2");
    while(high.pow(n).compareTo(b) == -1) high = high.multiply(two);
    low = high.divide(two);
    while(low.compareTo(high) == -1) {
      mid = high.add(low).divide(two);
      if(low.compareTo(mid) == -1 && mid.pow(n).compareTo(b) == -1) low = mid;
      else if(high.compareTo(mid) == 1 && mid.pow(n).compareTo(b) == 1) high = mid;
      else if(mid.pow(n).compareTo(b) == 0) return mid;
      else break;
    }
    return mid.add(BigInteger.ONE);
  }

}
