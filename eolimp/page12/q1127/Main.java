package page12.q1127;

import java.util.ArrayList;
import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), max = Integer.MIN_VALUE,
        ns[] = new int[n];

    HashMap<Integer, ArrayList<Integer>> m = new HashMap<Integer, ArrayList<Integer>>();

    for(int i=0; i<n; i++) {
      ns[i] = in.nextInt();
      max = Math.max(max, ns[i]);
      if(!m.containsKey(ns[i]))
        m.put(ns[i], new ArrayList<Integer>());
      m.get(ns[i]).add(i);
    }

    double sum = 0;
    for(int i=1; i<=max; i++) {
      sum += Math.log10(i);
      if(m.containsKey(i)) {
        for(int j : m.get(i)) {
          ns[j] = (int) (sum + 1);
        }
      }
    }

    for(long i : ns) System.out.println(i);
  }
}
