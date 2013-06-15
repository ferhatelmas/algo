package com.ferhatelmas.eolimp.page3.q62;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    BigInteger b = new BigInteger(new Scanner(System.in).next()), curr = BigInteger.ONE;
    for(int i=1; i<2001; i++) {
      curr = curr.multiply(new BigInteger(String.valueOf(i)));
      if(b.compareTo(curr) == 0) {
        System.out.println(i);
        break;
      }
    }
  }
}
