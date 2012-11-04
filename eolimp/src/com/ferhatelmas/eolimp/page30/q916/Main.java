package com.ferhatelmas.eolimp.page30.q916;

import java.util.Scanner;
import java.util.HashSet;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    HashSet<Integer> set = new HashSet<Integer>();

    int a = in.nextInt();
    int b = in.nextInt();
    int c = in.nextInt();
    int d = in.nextInt();
    int i, j;

    for(i=Math.min(a,b); i<=Math.max(a,b); i++)
      for(j=Math.min(c,d); j<=Math.max(c,d); j++)
        set.add(i*j);

    System.out.println(set.size());
  }

}