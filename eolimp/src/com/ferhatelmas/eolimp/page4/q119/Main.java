package com.ferhatelmas.eolimp.page4.q119;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine();
    BigInteger b = new BigInteger("2"), res = new BigInteger("2");

    int cnt = 0;
    while(!s.isEmpty()) {
      int k = res.toString().length();
      s = s.substring(k);
      cnt++;
      res = res.multiply(b);
    }
    System.out.println(cnt);
  }
}
