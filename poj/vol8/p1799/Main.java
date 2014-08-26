package vol8.p1799;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt(), cnt = 1;

    while(t-- > 0) {
      double R = in.nextDouble();
      int n = in.nextInt();

      double a = Math.sqrt(2*(1-Math.cos((2*Math.PI)/n)));

      System.out.format("Scenario #%d:\n%.3f\n\n", cnt++, R*a/(2+a));
    }
  }

}
