package page1.q44;

import java.util.HashMap;
import java.util.Scanner;

public class Main {

  private static HashMap<Integer, Integer> cache = new HashMap<Integer, Integer>();

  public static void main(String[] args) {
    System.out.println(f(new Scanner(System.in).nextInt()));
  }

  private static int f(int n) {
    if(n == 1) return 1;

    if(cache.containsKey(n)) return cache.get(n);
    int min = 1 + f(n-1);

    for(int i=2; i<=n/2; i++)
      if(n%i == 0)
        min = Math.min(min, f(i) + f(n/i));

    cache.put(n, min);
    return min;
  }
}
