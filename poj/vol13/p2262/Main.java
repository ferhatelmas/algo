package vol13.p2262;

import java.util.Arrays;
import java.util.Scanner;
import java.util.TreeSet;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    boolean sieve[] = new boolean[1000001];
    TreeSet<Integer> primes = new TreeSet<Integer>();
    Arrays.fill(sieve, true);
    for(int i=2; i<sieve.length; i++)
      if(sieve[i]) {
        primes.add(i);
        for(int j=2*i; j<sieve.length; j+=i)
          sieve[j] = false;
      }

    int n;
    while((n = in.nextInt()) != 0) {
      boolean flag = true;
      Integer i, x = n;
      while((i = primes.floor(x)) != null) {
        if(primes.contains(n - i)) {
          System.out.println(n + " = " + (n - i) + " + " + i);
          flag = false;
          break;
        } else {
          x = i-1;
        }
      }
      if(flag) System.out.println("Goldbach's conjecture is wrong.");
    }
  }
}
