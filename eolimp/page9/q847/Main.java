package page9.q847;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),
        ns[][] = new int[n][n];

    int x = 0, y = 0, w = 1;
    for(int i=1, k=n*n; i<=k; i++) {
      ns[x][y] = i;
      if(w == 1 && (x == 0 || y == n-1)) {
        if(y == n-1) x++;
        else y++;
        w = -1;
      } else if(w == -1 && (x == n-1 || y == 0)) {
        if(x == n-1) y++;
        else x++;
        w = 1;
      } else {
        x -= w;
        y += w;
      }
    }

    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
        if(j > 0) System.out.print(" ");
        System.out.print(ns[i][j]);
      }
      System.out.println();
    }
  }
}
