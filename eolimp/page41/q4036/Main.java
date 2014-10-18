package page41.q4036;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), ns[] = new int[n];

    for(int i=0; i<n; i++)
      ns[i] = in.nextInt();

    Arrays.sort(ns);
    System.out.print(ns[0]);
    for(int i=1; i<n; i++)
      System.out.print(" " + ns[i]);
    System.out.println();
  }
}
