package page40.q3970;

import java.util.HashMap;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k, p = -1, c = 0;
    HashMap<Integer, Integer> h = new HashMap<Integer, Integer>();
    for(int i=0; i<n; i++) {
      k = in.nextInt();
      if(p == -1) {
        p = k;
        c++;
      }
      else if(k == p) c++;
      else {
        h.put(p, c);
        p = k;
        c = 1;
      }
    }
    h.put(p, c);
    for(int i=in.nextInt(); i>0; i--) {
      k = in.nextInt();
      System.out.println(h.containsKey(k) ? h.get(k) : 0);
    }
  }
}
