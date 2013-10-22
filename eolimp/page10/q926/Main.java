package page10.q926;

import java.util.Scanner;
import java.util.Locale;
import java.text.DecimalFormat;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    in.useLocale(Locale.US);

    double d1=in.nextDouble();
    double d2=in.nextDouble();
    double d3=in.nextDouble();
    double d4=in.nextDouble();
    double d5=in.nextDouble();

    System.out.println(new DecimalFormat("#########0.0000").format(area(d1,d2,d5)+area(d3,d4,d5)).replace(",", "."));
  }

  private static double area(double a, double b, double c) {
    double s = (a+b+c)/2;
    return Math.sqrt(s*(s-a)*(s-b)*(s-c));
  }

}