package page32.q3174;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt(), ns[][] = new int[1000][1000];

    for(int i=0; i<ns.length; i++)
      ns[ns.length-1][i] = ns[i][0] = 1;

    for(int i=ns.length-2; i>-1; i--) {
      for(int j=1; j<ns.length; j++) {
        ns[i][j] = (ns[i][j-1] + ns[i+1][j] + ns[i+1][j-1]) % 1000003;
      }
    }

    while(t-- > 0) {
      int n = in.nextInt();
      System.out.println(ns[1000-n][n-1]);
    }
  }
}
