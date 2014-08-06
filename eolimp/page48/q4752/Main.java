package page48.q4752;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int m = in.nextInt(), n = in.nextInt(),
        as[][] = new int[m][n], bs[][] = new int[m][n], cnt;

    cnt = 0;
    for(int i=m-1; i>-1; i--) {
      for(int j=0; j<n; j++) {
        as[i][j] = ++cnt;
      }
    }

    cnt = 0;
    for(int j=0; j<n; j++) {
      for(int i=m-1; i>-1; i--) {
        bs[i][j] = ++cnt;
      }
    }

    cnt = 0;
    for(int i=0; i<m; i++) {
      for(int j=0; j<n; j++) {
        if(as[i][j] == bs[i][j]) cnt++;
      }
    }

    System.out.println(cnt);
  }
}
