package page10.q954;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double a = in.nextDouble(), b = in.nextDouble(), h = in.nextDouble();
    System.out.printf(Locale.US, "%.2f\n", 2 * (a + b) * Math.sqrt(Math.pow((a - b)/2, 2) + h*h));
  }
}
