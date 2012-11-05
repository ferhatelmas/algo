package com.ferhatelmas.eolimp.page31.q928;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n=in.nextInt(), tmp;
    int min = Integer.MAX_VALUE, max = Integer.MIN_VALUE;
    for(int i=0; i<n; i++) {
      tmp = in.nextInt();
      if(tmp < min) min = tmp;
      if(tmp > max) max = tmp;
    }
    System.out.println(min+max);
  }

}