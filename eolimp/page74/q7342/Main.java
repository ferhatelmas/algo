package page74.q7342;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double a = in.nextDouble(), b = in.nextDouble(),
           m = in.nextDouble(), n = in.nextDouble(),
           r = Math.max(Math.min(m/a, n/b), Math.min(n/a, m/b));
    System.out.printf(Locale.US, "%.3f %.3f\n", r*a, r*b);
  }
}
