package page48.q4749;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), m = in.nextInt();
    int ns[][] = new int[n][m];

    for(int i=0; i<n; i++)
      for(int j=0; j<m; j++)
        ns[i][j] = in.nextInt();

    int sum = 0;
    for(int i=0; i<n; i++)
      for(int j=0; j<m; j++)
        sum += in.nextInt() * ns[i][j];
    System.out.println(sum);
  }
}
