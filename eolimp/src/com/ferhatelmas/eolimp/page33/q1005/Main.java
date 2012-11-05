package com.ferhatelmas.eolimp.page33.q1005;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    StringBuilder sb=new StringBuilder();
    int t=in.nextInt(), i, m, n, k;

    for(i=0; i<t; i++) {
      m=in.nextInt();
      n=in.nextInt();

      k=m-(m/(n+1))*(n+1);
      if(k<=n && k!=0) sb.append('1');
      else sb.append('2');
    }

    System.out.println(sb.toString());
  }

}