package page51.q5090;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[][] = new int[n][n],
        m = 0, mi = -1, mj = -1;

    for(int i=0; i<n; i++) {
      int t = 0;
      for(int j=0; j<n; j++) {
        ns[i][j] = in.nextInt();
        t += ns[i][j];
      }
      if(t > m) {
        m = t;
        mi = i;
      }
    }

    m = Integer.MAX_VALUE;
    for(int j=0; j<n; j++) {
      int t = 0;
      for(int i=0; i<n; i++) {
        t += ns[i][j];
      }
      if(t < m) {
        m = t;
        mj = j;
      }
    }

    System.out.println(ns[mi][mj]);
  }
}
