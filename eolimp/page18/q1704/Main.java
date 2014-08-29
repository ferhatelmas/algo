package page18.q1704;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();
    long ns[][] = new long[n][m];

    ns[n-1][0] = 1;
    for(int i=n-1; i>-1; i--) {
      for(int j=0; j<m; j++) {
        if(i == n-1 && j == 0) continue;
        ns[i][j] = (i < n-1 ? ns[i+1][j] : 0) + (j > 0 ? ns[i][j-1] : 0);
      }
    }
    System.out.println(ns[0][m-1]);
  }
}
