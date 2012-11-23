package com.ferhatelmas.eolimp.page72.q2314;

import java.util.Scanner;
import java.util.TreeSet;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n;
    TreeSet<Integer> pq = new TreeSet<Integer>();
    while((n=in.nextInt()) != 0)
      pq.add(n);
    System.out.println(pq.lower(pq.last()));
  }

}
