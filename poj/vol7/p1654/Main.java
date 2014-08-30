package vol7.p1654;

import java.util.HashMap;
import java.util.Scanner;

public class Main {

  private static HashMap<Character, Integer[]> m = new HashMap<Character, Integer[]>();
  static {
    m.put('1', new Integer[]{-1, -1});
    m.put('2', new Integer[]{0, -1});
    m.put('3', new Integer[]{1, -1});
    m.put('4', new Integer[]{-1, 0});
    m.put('6', new Integer[]{1, 0});
    m.put('7', new Integer[]{-1, 1});
    m.put('8', new Integer[]{0, 1});
    m.put('9', new Integer[]{1, 1});
  }

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    while(n-- > 0) {
      long sum = 0;
      int i = 0, j = 0;
      String s = in.next();
      for(int k=0, l=s.length()-1; k<l; k++) {
        Integer d[] = m.get(s.charAt(k));
        sum += i * (j + d[1]) - (i + d[0]) * j;
        i += d[0];
        j += d[1];
      }
      if(sum%2 == 0)
        System.out.println(Math.abs(sum / 2));
      else
        System.out.println(Math.abs(sum / 2.0));
    }
  }
}
