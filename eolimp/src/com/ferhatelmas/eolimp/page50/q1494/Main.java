package com.ferhatelmas.eolimp.page50.q1494;

import java.util.HashSet;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt() + in.nextInt();
    HashSet<Integer> cache = new HashSet<Integer>();

    for(int i=0; i<k; i++)
      cache.add(in.nextInt());

    int cnt = 0;
    StringBuilder sb = new StringBuilder();
    for(int i=1; i<=n; i++)
      if(!cache.contains(i)) {
        if(cnt > 0) sb.append(" ");
        sb.append(i);
        cnt++;
      }

    System.out.println(cnt);
    System.out.println(sb.toString());
  }
}
