package page51.q5091;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),
        ns[][] = new int[n][2];
    ns[0][0] = 1; ns[0][1] = 1;

    for(int i=1; i<n; i++) {
      for(int j=0; j<2; j++) {
        if(j == 0) {
          ns[i][j] = ns[i-1][j+1];
        } else {
          ns[i][j] = ns[i-1][j-1] + ns[i-1][j];
        }
      }
    }
    System.out.println((long)ns[n-1][0] + ns[n-1][1]);
  }
}
