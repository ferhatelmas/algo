package page24.q2375;

import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), c = in.nextInt(), ss = 0, cs = 0, bs = 0;

    for(int i=0; i<n; i++) {
      int s = in.nextInt();
      String type = in.next();
      if("bedroom".equals(type)) cs += s;
      else if("balcony".equals(type)) bs += s;
      ss += s;
    }

    double cost = c * (ss - (bs/2.0));
    System.out.format(Locale.US, "%d\n%d\n%s\n", ss, cs,
        cost == (int)cost ? String.format("%d", (int)cost) : cost);
  }
}
