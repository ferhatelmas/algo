package com.ferhatelmas.poj.vol12.p2140;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    int sum, cnt = 0;
    for(int i=1; i<=n; i++) {
      sum = 0;
      for(int j=i; j<=n; j++) {
        if(sum >= n) break;
        sum += j;
      }
      if(sum == n) cnt++;
    }
    System.out.println(cnt);
  }

}
