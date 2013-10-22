package page22.q2132;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double x = in.nextDouble(), y = in.nextDouble(),
           a = in.nextDouble(), b = in.nextDouble(), c = in.nextDouble();
    System.out.println(Math.abs(a*x + b*y + c) < 0.00001 ? "YES" : "NO");
  }
}
