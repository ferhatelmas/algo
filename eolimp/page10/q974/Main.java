package page10.q974;

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
        for (int j = 0; j < n; j++)
          if (ns[i][j] > ns[i][k] + ns[k][j])
            ns[i][j] = ns[i][k] + ns[k][j];

    for (int i = 0; i < n; i++) {
      StringBuilder sb = new StringBuilder();
      for (int j = 0; j < n; j++)
        sb.append(' ').append(ns[i][j]);
      System.out.println(sb.substring(1));
    }
  }
}
