package com.ferhatelmas.eolimp.page93.q2425;

import java.util.ArrayList;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    long n = new Scanner(System.in).nextLong();
    ArrayList<Long> fibs = generate_fibs(n);

    StringBuilder sb = new StringBuilder();
    for(int i=fibs.size()-1; i>-1; i--) {
      long l = fibs.get(i);
      if(n >= l) {
        sb.append('1');
        n -= l;
      } else
        sb.append('0');
    }
    System.out.println(sb.toString());
  }

  private static ArrayList<Long> generate_fibs(long n) {
    ArrayList<Long> fibs = new ArrayList<Long>();
    long a = 1L, b = 1L;
    while(a <= n) {
      fibs.add(a);
      long t = a;
      a += b;
      b = t;
    }
    return fibs;
  }
}
