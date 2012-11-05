package com.ferhatelmas.eolimp.page17.q488;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int n = new Scanner(System.in).nextInt(), cnt=1;
    int[][] buf=new int[n][n];

    for(int i=0; i<n; i++) {
      if(i%2==0) {
        for(int j=0; j<n; j++) {
          buf[i][j]=cnt;
          cnt++;
        }
      } else {
        for(int j=n-1; j>-1; j--) {
          buf[i][j]=cnt;
          cnt++;
        }
      }
    }

    for(int i=0; i<n; i++) {
      for(int j=0; j<n-1; j++)
        System.out.print(buf[i][j] + " ");
      System.out.println(buf[i][n-1]);
    }
  }

}