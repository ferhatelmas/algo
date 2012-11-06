package com.ferhatelmas.eolimp.page48.q1463;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in=new Scanner(System.in);

    int n = in.nextInt();
    int[][] buf = new int[n][n];

    int i, j, maxRow = 0, maxColumn = 0;
    long sum, max;

    for(i=0; i<n; i++)
      for(j=0; j<n; j++)
        buf[i][j] = in.nextInt();

    max = Long.MIN_VALUE;
    for(i=0; i<n; i++) {
      sum = 0;
      for(j=0; j<n; j++)
        sum += buf[i][j];

      if(sum > max) {
        maxRow = i;
        max = sum;
      }
    }

    max = Long.MAX_VALUE;
    for(i=0; i<n; i++) {
      sum=0;
      for(j=0; j<n; j++)
        sum += buf[j][i];

      if(sum < max) {
        maxColumn = i;
        max = sum;
      }
    }

    System.out.println(buf[maxRow][maxColumn]);
  }

}