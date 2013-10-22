package page12.q1146;

import java.util.HashMap;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();

    int sum = 0;
    for(int n=2; n<501; n++) {
      for(int i=1; i<n; i++) {
        sum += gcd(n, i);
      }
      cache.put(n, sum);
    }

    while((sum = in.nextInt()) != 0)
      System.out.println(cache.get(sum));
  }

  private static int gcd(int a, int b) {
    return b == 0 ? a : gcd(b, a%b);
  }

}
