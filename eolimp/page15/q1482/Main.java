package page15.q1482;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(),
        as[][] = new int[a][b];

    for(int i=0; i<a; i++) {
      for(int j=0; j<b; j++) {
        as[i][j] = in.nextInt();
      }
    }

    int c = in.nextInt(), d = in.nextInt(),
        cs[][] = new int[c][d];
    if(c != b)
      System.out.println(-1);
    else {
      for(int i=0; i<c; i++) {
        for(int j=0; j<d; j++) {
          cs[i][j] = in.nextInt();
        }
      }
      System.out.println(a + " " + d);
      for(int i=0; i<a; i++) {
        for(int j=0; j<d; j++) {
          int sum = 0;
          for(int k=0; k<b; k++) {
            sum += as[i][k] * cs[k][j];
          }
          System.out.print(sum + (j == d-1 ? "\n" : " "));
        }
      }
    }
  }
}
