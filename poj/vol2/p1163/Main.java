package vol2.p1163;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[][] = new int[n][n], max = 0;

    for(int i=0; i<n; i++) {
      for(int j=0; j<i+1; j++) {
        ns[i][j] = in.nextInt();
        if(i > 0) {
          ns[i][j] += Math.max(ns[i-1][j], j > 0 ? ns[i-1][j-1] : 0);
        }
        if(i == n-1) {
          max = Math.max(max, ns[i][j]);
        }
      }
    }
    System.out.println(max);
  }
}
