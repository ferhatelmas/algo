package page51.q5052;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), j = 1 << (in.nextInt() - 1);
    System.out.println((n & j) == j ? "YES" : "NO");
  }
}
