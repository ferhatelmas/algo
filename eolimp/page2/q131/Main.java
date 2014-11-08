package page2.q131;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    HashMap<Character, Integer> m = getMap(in.next());

    int t = in.nextInt(), r = 0;
    while(t-- > 0) {
      if(isProducible(m, getMap(in.next())))
        r++;
    }
    System.out.println(r);
  }

  private static boolean isProducible(HashMap<Character, Integer> m1, HashMap<Character, Integer> m2) {
    for(char c : m2.keySet()) {
      if(!m1.containsKey(c) || m1.get(c) < m2.get(c))
        return false;
    }
    return true;
  }

  private static HashMap<Character, Integer> getMap(String s) {
    HashMap<Character, Integer> m = new HashMap<Character, Integer>();
    for(char c : s.toCharArray())
      m.put(c, 1 + (m.containsKey(c) ? m.get(c) : 0));
    return m;
  }
}
