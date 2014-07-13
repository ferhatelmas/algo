package page6.q568;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in).useLocale(Locale.US);

    double d = 0; int i = 0;
    while(in.hasNextDouble()) {
      d += in.nextDouble();
      i++;
    }
    System.out.printf(Locale.US, "%.2f\n", d/i);
  }
}
