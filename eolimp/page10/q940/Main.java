package page10.q940;

import java.util.Locale;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int x1 = in.nextInt(), y1 = in.nextInt(),
        x2 = in.nextInt(), y2 = in.nextInt(),
        x3 = in.nextInt(), y3 = in.nextInt();

    System.out.format(Locale.US,  "%.1f\n", getArea(getDist(x1, y1, x2, y2),
                                                    getDist(x1, y1, x3, y3),
                                                    getDist(x2, y2, x3, y3)));
  }

  private static double getDist(int x1, int y1, int x2, int y2) {
    return Math.sqrt((x1 - x2) * (x1 - x2) + (y1 - y2) * (y1 - y2));
  }

  private static double getArea(double d1, double d2, double d3) {
    double s = (d1+d2+d3) / 2;
    return Math.sqrt(s * (s-d1) * (s-d2) * (s-d3));
  }
}
