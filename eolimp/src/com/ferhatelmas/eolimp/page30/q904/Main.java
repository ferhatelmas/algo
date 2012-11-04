package com.ferhatelmas.eolimp.page30.q904;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    int i, tmp;
    int[] buf = new int[n];
    for(i=0; i<n; i++) {
      tmp = in.nextInt();
      if(tmp>=0) tmp+=2;
      buf[i] = tmp;
    }

    for(i=0; i<buf.length-1; i++)
      System.out.print(buf[i] + " ");

    System.out.println(buf[buf.length-1]);
  }

}