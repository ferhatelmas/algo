package com.ferhatelmas.eolimp.page84.q2631;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = Integer.parseInt(in.nextLine());
    while(t-- > 0) {
      String[] ss = in.nextLine().split(" ");
      int[] ns = new int[ss.length];
      for(int i=0; i<ss.length; i++) ns[i] = Integer.parseInt(ss[i]);
      Arrays.sort(ns);
      System.out.println(findMaxGcd(ns));
    }
  }

  private static int findMaxGcd(int[] ns) {
    int max = 1;
    for(int i=0; i<ns.length; i++)
      for(int j=i+1; j<ns.length; j++)
        max = Math.max(max, gcd(Math.max(ns[i], ns[j]), Math.min(ns[i], ns[j])));
    return max;
  }

  private static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a%b);
  }
}
