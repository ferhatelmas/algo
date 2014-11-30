package page26.q2544;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    HashMap<Integer, ArrayList<Double>> m = new HashMap<Integer, ArrayList<Double>>();
    HashMap<Integer, HashMap<String, Integer>> h = new HashMap<Integer, HashMap<String, Integer>>();

    while(n-- > 0) {
      int q = in.nextInt();
      String u = in.next();
      double t = in.nextDouble();

      if(!m.containsKey(q)) {
        m.put(q, new ArrayList<Double>());
        h.put(q, new HashMap<String, Integer>());
      }

      ArrayList<Double> ms = m.get(q);
      HashMap<String, Integer> hs = h.get(q);
      if(hs.containsKey(u)) {
        if(ms.get(hs.get(u)) <= t) {
          System.out.println("submission ignored");
          continue;
        } else {
          int j = add(ms, hs.get(u), t);
          update(hs, j, hs.get(u));
          hs.put(u, j);
        }
      } else {
        int j = add(ms, -1, t);
        update(hs, j, ms.size());
        hs.put(u, j);
      }

      System.out.printf("%d %s %.3f %.3f %d\n", q, u, t, ms.get(0), hs.get(u)+1);
    }
  }

  private static int add(ArrayList<Double> ls, int i, double s) {
    if(i == -1) {
      ls.add(s);
      i = ls.size() - 1;
    } else {
      ls.set(i, s);
    }

    s = ls.get(i);
    while(i > 0 && ls.get(i-1) > s) {
      ls.set(i, ls.get(i-1));
      i--;
    }
    ls.set(i, s);
    return i;
  }

  private static void update(HashMap<String, Integer> m, int s, int e) {
    for(String ss : m.keySet()) {
      int v = m.get(ss);
      if(v >= s && v < e)
        m.put(ss, v + 1);
    }
  }
}
