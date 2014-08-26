package vol1.p1003;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    double d = in.nextDouble();
    while(d >= 0.01) {
      System.out.println(getCardNumber(d) + " card(s)");
      d = in.nextDouble();
    }
  }

  private static int getCardNumber(double d) {
    int n = 2;
    double sum = 0;
    while(sum < d) {
      sum += 1.0/n;
      n++;
    }
    return n-2;
  }

}
