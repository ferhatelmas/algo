package page4.q352;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    double d = Double.MAX_VALUE;
    for(String s : new Scanner(System.in).nextLine().split("\\s")) {
      double dd = Double.parseDouble(s);
      if(dd < d) d = dd;
    }
    System.out.printf(Locale.US, "%.2f\n", d);
  }
}
