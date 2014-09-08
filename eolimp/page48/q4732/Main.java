package page48.q4732;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    HashMap<Integer, Integer> h1 = new HashMap<Integer, Integer>();
    HashMap<Integer, Integer> h2 = new HashMap<Integer, Integer>();
    h1.put(0, 0);h2.put(0, 0);
    h1.put(1, 1);h2.put(1, 1);
    for(int i=2; i<47; i++) {
      int x = h1.get(i-1) + h1.get(i-2);
      h1.put(i, x);
      h2.put(x, i-1);
    }

    int n = new Scanner(System.in).nextInt();
    System.out.println(h2.get(n));
  }
}
