package page5.q418;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    in.useLocale(Locale.US);
    double sum = 0;
    for(int i=0; i<3; i++)
      sum += Math.sqrt(in.nextDouble());
    System.out.format(Locale.US, "%.8f\n", Math.pow(sum, 2));
  }
}
