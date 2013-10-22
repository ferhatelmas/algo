package page10.q948;

import java.util.Locale;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double d = in.nextDouble(), s = in.nextDouble();

    System.out.format(Locale.US,  "%.3f %.3f\n", getArea(d, s), getVolume(d, s));
  }

  private static double getArea(double d, double s) {
    return d*d + 2*d*Math.sqrt(s*s - d*d*0.25);
  }

  private static double getVolume(double d, double s) {
    double h = Math.sqrt(s*s-d*d*0.5);
    return (1/3.0) * d * d * h;
  }
}
