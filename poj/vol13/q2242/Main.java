package vol13.q2242;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double coors[] = new double[6];

    while(in.hasNextDouble()) {
      for(int i=0; i<coors.length; i++)
        coors[i] = in.nextDouble();

      System.out.printf("%.2f\n", Math.PI * d(coors));
    }
  }

  private static double d(double x[]) {
    double a = l(x[0], x[1], x[2], x[3]),
           b = l(x[0], x[1], x[4], x[5]),
           c = l(x[2], x[3], x[4], x[5]),
           s = (a + b + c) / 2;
    return (a*b*c) / (2 * Math.sqrt(s * (s-a) * (s-b) * (s-c)));
  }

  private static double l(double x1, double y1, double x2, double y2) {
    return Math.sqrt(Math.pow(x1-x2, 2) + Math.pow(y1-y2, 2));
  }
}
