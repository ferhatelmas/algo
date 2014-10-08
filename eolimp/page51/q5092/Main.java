package page51.q5092;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),
        ns[][] = new int[n][2];
    if(n < 2) {
      System.out.println(n);
      return;
    }
    ns[0][0] = 1; ns[0][1] = 1;

    for(int i=1; i<n; i++) {
      for(int j=0; j<2; j++) {
        if(j == 0) {
          ns[i][j] = ns[i-1][j] + (i > 1 ? ns[i-2][j+1] : 0);
        } else {
          ns[i][j] = ns[i][j-1];
        }
      }
    }
    System.out.println(ns[n-1][0]);
  }
}
