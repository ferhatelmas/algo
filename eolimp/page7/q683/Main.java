package page7.q683;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();
    int ns[][] = new int[2][m];
    StringBuilder sb = new StringBuilder();
    for(int i=0; i<n; i++) {
      for(int j=0; j<m; j++) {
        int r = i%2;
        ns[r][j] = in.nextInt();
        if(j > 0) ns[r][j] += ns[r][j-1];
        if(i > 0) ns[r][j] += ns[1-r][j];
        if(i > 0 && j > 0) ns[r][j] -= ns[1-r][j-1];
        sb.append(ns[r][j]);
        if(j < m-1) sb.append(' ');
      }
      System.out.println(sb.toString());
      sb = new StringBuilder();
    }
  }
}
