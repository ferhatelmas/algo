package page2.q143;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double[] points = new double[8];
    for(int i=0; i<points.length; i++)
      points[i] = in.nextDouble();
    double[] sides = new double[6];
    for(int i=0; i<3; i++)
      for(int j=i+1; j<=3; j++)
      sides[i+j-(i==0?1:0)] = getLength(points, i, j);
    System.out.println(isEqual(sides) ? 1 : 0);
  }

  private static double getLength(double[] p, int i, int j) {
    return Math.sqrt(Math.pow(p[2*i]-p[2*j], 2) + Math.pow(p[2*i+1]-p[2*j+1], 2));
  }

  private static double getArea(double[] p, int[] k) {
    double s = 0;
    for(int i : k)
      s += p[i];
    s /= 2;
    double t = s;
    for(int i : k)
      t *= (s-p[i]);
    return Math.sqrt(t);
  }

  private static boolean isEqual(double[] s) {
    return getArea(s, new int[]{0, 1, 3}) + getArea(s, new int[]{0, 2, 4}) +
           getArea(s, new int[]{1, 2, 5}) - getArea(s, new int[]{3, 4, 5}) < 0.001;
  }
}
