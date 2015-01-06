package page74.q7368;

import java.util.HashMap;
import java.util.Locale;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), t = in.nextInt();
    boolean f = true;
    while (t-- > 0) {
      int max = Integer.MIN_VALUE, min = Integer.MAX_VALUE, s = 0;
      HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();
      for(int i=0; i<n; i++) {
        int c = in.nextInt();
        h.put(c, 1 + (h.containsKey(c) ? h.get(c) : 0));
        s += c;
        max = Math.max(max, c);
        min = Math.min(min, c);
      }
      s -= (h.get(max) * max + h.get(min) * min);
      if (!f) System.out.print(" ");
      else f = !f;
      System.out.printf(Locale.US, "%.2f", s / (double)(n-h.get(max)-h.get(min)));
    }
    System.out.println();
  }
}
