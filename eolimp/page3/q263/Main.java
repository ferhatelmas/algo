package page3.q263;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(),
        ns[][] = new int[n][3], m = 12345;

    ns[0][0] = ns[0][1] = 1;
    ns[0][2] = 0;
    for(int i=1; i<n; i++) {
      ns[i][0] = (ns[i-1][0] + ns[i-1][1] + ns[i-1][2]) % m;
      ns[i][1] = ns[i-1][0];
      ns[i][2] = ns[i-1][1];
    }

    System.out.println((ns[n-1][0] + ns[n-1][1] + ns[n-1][2]) % m);
  }
}
