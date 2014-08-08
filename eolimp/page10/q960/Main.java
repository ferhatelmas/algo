package page10.q960;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double r1 = in.nextDouble(), r2 = in.nextDouble(), h = in.nextDouble();
    System.out.printf(Locale.US, "%.2f\n", Math.PI * (r1 + r2) * Math.sqrt(Math.pow(r1 - r2, 2) + h * h) +
        Math.PI * (r1 * r1 + r2 * r2));
  }
}
