package page39.q3836;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), t = in.nextInt();
    HashMap<String, String> h = new HashMap<String, String>();

    while(n-- > 0)
      h.put(in.next(), in.next());

    while(t-- > 0) {
      String s = in.next();
      if(h.containsKey(s)) System.out.println(h.get(s));
      else if(s.matches(".*[^aeiou]y")) System.out.println(s.substring(0, s.lastIndexOf('y')) + "ies");
      else if(s.matches(".*(?:o|s|ch|sh|x)")) System.out.println(s + "es");
      else System.out.println(s + "s");
    }
  }
}
