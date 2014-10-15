package page41.q4097;

import java.util.Calendar;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long min = Long.MAX_VALUE, max = Long.MIN_VALUE, t = in.nextInt();
    String mins = "", maxs = "";

    Calendar c = Calendar.getInstance();
    while(t-- > 0) {
      String s = in.next();
      int d = in.nextInt(), m = in.nextInt(), y = in.nextInt();
      c.set(y, m, d);
      long l = c.getTimeInMillis();
      if(l > max) {
        max = l;
        maxs = s;
      }

      if(l < min) {
        min = l;
        mins = s;
      }
    }

    System.out.println(maxs);
    System.out.println(mins);
  }
}
