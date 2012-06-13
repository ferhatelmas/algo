package com.ferhatelmas.euler.page7;

import java.util.HashSet;

public class Question346 {

  public static void main(String[] args) {

    HashSet<Long> set = new HashSet<Long>();

    for(int i=2; i<1000000; i++) {
      int len = 3;
      long val = getVal(i, len);
      while(val < 1000000000000L) {
        set.add(val);
        val = getVal(i, ++len);
      }
    }

    long sum = 1;
    for(long l : set) sum += l;
    System.out.println(sum);
  }

  private static long getVal(int base, int len) {
    long val = 1, mul = 1;

    for(int i=1; i<len; i++) {
      mul *= base;
      val += mul;
    }

    return val;
  }

}
