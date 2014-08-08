package page10.q958;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double b = in.nextDouble(), a = (in.nextDouble() / 180) * Math.PI,
           h = b * Math.sin(a), x = 2 * b * Math.cos(a) / Math.sqrt(2);

    System.out.printf(Locale.US, "%.3f\n", x*x + 2 * x * Math.sqrt(Math.pow(x/2, 2) + h*h));
  }
}
