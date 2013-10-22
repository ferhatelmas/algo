package page5.q428;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      double r = in.nextDouble(), x = Math.abs(in.nextDouble()), y = in.nextDouble();
      System.out.format(Locale.US, "%.2f\n", (r * x) / (2*r - y));
    }
  }
}
