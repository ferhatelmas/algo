package com.ferhatelmas.eolimp.page41.q1247;

import java.util.LinkedList;
import java.util.ListIterator;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    while(in.hasNext()) {
      int n = in.nextInt();
      if(n == 0) break;

      System.out.println(n + " " + getLcmCardinality(n, getDivisors(n)));
    }
  }

  private static LinkedList<Integer> getDivisors(int n) {
    int i = 2, cnt;
    LinkedList<Integer> powers = new LinkedList<Integer>();
    while(i <= n) {
      cnt = 0;
      while(n%i == 0) {
        cnt++;
        n /= i;
      }
      if(cnt > 0) {
        powers.addLast(i);
        powers.addLast(cnt);
      }
      i++;
    }
    return powers;
  }

  private static int getLcmCardinality(int n, LinkedList<Integer> powers) {
    if(n == 1) return 1;

    int p1 = powers.removeFirst();
    int n1 = powers.removeFirst();

    ListIterator li = powers.listIterator();
    int i = 0, j, mul = n1;
    while(li.hasNext()) {
      j = (Integer)li.next();
      if(i%2 == 1) mul *= (2*j+1);
      i++;
    }

    return mul + getLcmCardinality(n/(int)Math.pow(p1, n1), powers);
  }

}
