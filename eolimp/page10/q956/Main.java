package page10.q956;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double v = in.nextDouble(), h = in.nextDouble(), b = Math.sqrt(3 * v / h);
    System.out.printf(Locale.US, "%.1f\n", 2 * b * Math.sqrt(Math.pow(b/2, 2) + h*h));
  }
}
