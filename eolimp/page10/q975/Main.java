package page10.q975;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(),
        ns[][] = new int[n][n];

    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        ns[i][j] = in.nextInt();

    for (int k = 0; k < n; k++)
      for (int i = 0; i < n; i++)
        for (int j = 0; j < n; j++) {
          if (Math.min(ns[i][k], ns[k][j]) == -1) continue;
          if (ns[i][j] == -1 || ns[i][j] > ns[i][k] + ns[k][j])
            ns[i][j] = ns[i][k] + ns[k][j];
        }

    int max = Integer.MIN_VALUE;
    for (int i = 0; i < n; i++)
      for (int j = 0; j < n; j++)
        max = Math.max(max, ns[i][j]);
    System.out.println(max);
  }
}

