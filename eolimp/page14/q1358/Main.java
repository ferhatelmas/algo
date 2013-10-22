package page14.q1358;

import java.util.Arrays;
import java.util.HashSet;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    long[] ns = new long[n];
    long max = Long.MIN_VALUE;

    for(int i=0; i<n; i++) {
      ns[i] = in.nextLong();
      max = Math.max(max, ns[i]);
    }
    Arrays.sort(ns);

    HashSet<Long> fibs = new HashSet<Long>();
    long l, l1 = 0, l2 = 1;
    while((l = l1 + l2) <= max) {
      l1 = l2;
      l2 = l;
      fibs.add(l);
    }
    int cnt = 0;
    for(long v : ns) if(fibs.contains(v)) cnt++;
    System.out.println(cnt);
  }

}
