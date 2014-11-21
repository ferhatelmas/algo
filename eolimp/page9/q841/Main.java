package page9.q841;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),
        ns[][] = new int[n][n];

    for(int i=0; i<n; i++)
      Arrays.fill(ns[i], -1);

    int x = 0, y = 0, w = 0;
    for(int i=1, k=n*n; i<=k; i++) {
      ns[x][y] = i;
      switch (w) {
        case 0:
          if(y == n-1 || ns[x][y+1] != -1) {
            w = 1;
            x++;
          } else
            y++;
          break;
        case 1:
          if(x == n-1 || ns[x+1][y] != -1) {
            w = 2;
            y--;
          } else
            x++;
          break;
        case 2:
          if(y == 0 || ns[x][y-1] != -1) {
            w = 3;
            x--;
          } else
            y--;
          break;
        case 3:
          if(x == 0 || ns[x-1][y] != -1) {
            w = 0;
            y++;
          } else
            x--;
          break;
      }
    }

    StringBuilder sb = new StringBuilder();
    for(int i=0; i<n; i++) {
      for(int j=0; j<n; j++) {
        if (j != 0) sb.append(' ');
        sb.append(ns[i][j]);
      }
      sb.append('\n');
    }
    System.out.print(sb.toString());
  }
}
