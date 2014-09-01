package page19.q1812;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String s;

    while(!(s = in.nextLine()).equals("#")) {
      int l = s.length();
      HashMap<Character, Integer> m = new HashMap<Character, Integer>();
      m.put('A', 0); m.put('Y', 0); m.put('N', 0); m.put('P', 0);
      for(int i=0; i<l; i++)
        m.put(s.charAt(i), m.get(s.charAt(i)) + 1);


      if(m.get('A') >= l/2 + l%2) System.out.println("need quorum");
      else {
        int y = m.get('Y'), n = m.get('N');
        System.out.println(y == n ? "tie" : (y > n ? "yes" : "no"));
      }
    }
  }
}
