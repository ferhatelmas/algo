package page7.q684;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();
    long ns[][] = new long[n][m];

    for(int i=0; i<n; i++) {
      for(int j=0; j<m; j++) {
        long l = in.nextLong();
        if(i == 0 && j == 0) ns[i][j] = l;
        else if(i == 0) ns[i][j] = l + ns[i][j-1];
        else ns[i][j] = ns[i-1][j] + (j > 0 ? ns[i][j-1] - ns[i-1][j-1] : 0) + l;
      }
    }

    int t = in.nextInt();
    while(t-- > 0) {
      int is[] = new int[4];
      for(int i=0; i<is.length; i++)
        is[i] = in.nextInt() - 1;
      System.out.println(ns[is[2]][is[3]] -
          (is[1] > 0 ? ns[is[2]][is[1]-1] : 0) -
          (is[0] > 0 ? ns[is[0]-1][is[3]] : 0) +
          (is[0] > 0 && is[1] > 0 ? ns[is[0]-1][is[1]-1] : 0));
    }
  }
}
