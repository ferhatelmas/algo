package com.ferhatelmas.eolimp.page44.q1325;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = in.nextInt(), m=in.nextInt(), k=in.nextInt();
    int[] holes=new int[n];
    long mul=1;

    for(int i=0; i<n; i++) holes[i]=in.nextInt();
    for(int i=Math.min(m,k); i<=Math.max(m,k); i++) mul*=holes[i-1];

    System.out.println(mul);
  }
}
