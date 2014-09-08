package page48.q4731;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n, m = Integer.MIN_VALUE;

    HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();
    while((n = in.nextInt()) != 0) {
      m = Math.max(m, n);
      h.put(n, 1 + (h.containsKey(n) ? h.get(n) : 0));
    }
    System.out.println(h.get(m));
  }
}
