package com.ferhatelmas.eolimp.page41.q1247;

import java.util.LinkedList;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while(in.hasNext()) {
      int n = in.nextInt();
      if(n == 0) break;

      System.out.println(n + " " + getLcmCardinality(getDivisors(n)));
    }
  }

  private static Integer[] getDivisors(int n) {
    int i = 2, cnt;
    LinkedList<Integer> powers = new LinkedList<Integer>();
    while(i <= n) {
      cnt = 0;
      while(n%i == 0) {
        cnt++;
        n /= i;
      }
      if(cnt > 0) {
        powers.addLast(2*cnt+1);
      }
      i++;
    }
    return powers.toArray(new Integer[powers.size()]);
  }

  private static int getLcmCardinality(Integer[] powers) {
    int sum = 1, mul;
    for(int i=0; i<powers.length; i++) {
      mul = powers[i]/2;
      for(int j=i+1; j<powers.length; j++) {
        mul *= powers[j];
      }
      sum += mul;
    }
    return sum;
  }

}
