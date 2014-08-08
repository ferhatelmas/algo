package page10.q952;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double a = in.nextDouble(), h = in.nextDouble();
    System.out.printf(Locale.US, "%.1f\n", a * a + 2 * a * Math.sqrt(Math.pow(a/2, 2) + h*h));
  }
}
