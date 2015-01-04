package page74.q7341;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(c(in.nextInt()) * c(in.nextInt()));
  }

  private static long c(int n) {
    return n * (n+1) / 2;
  }
}
