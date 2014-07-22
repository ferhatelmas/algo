package page8.q769;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    HashMap<Integer, Integer> x = new HashMap<Integer, Integer>(),
                              y = new HashMap<Integer, Integer>();
    int a = -1, b = -1;
    for(int i=0; i<3; i++) {
      a = in.nextInt();
      b = in.nextInt();
      x.put(a, x.containsKey(a) ? 2 : 1);
      y.put(b, y.containsKey(b) ? 2 : 1);
    }

    for(int i : x.keySet()) if(x.get(i) == 1) a = i;
    for(int i : y.keySet()) if(y.get(i) == 1) b = i;
    System.out.println(a + " " + b);
  }
}
