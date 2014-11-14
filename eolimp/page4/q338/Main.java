package page4.q338;

import java.util.ArrayList;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  private static ArrayList<Integer> primes = new ArrayList<Integer>();

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), c = 0;
    boolean b[] = new boolean[n+1];
    Arrays.fill(b, true);

    for(int i=2; i<b.length; i++)
      if(b[i]) {
        primes.add(i);
        for(int j=2*i; j<b.length; j+=i)
          b[j] = false;
      }

    for(int i=2; i<=n; i++)
      c += totient(i);

    System.out.println(c);
  }

  private static int totient(int n) {
    int r = n;
    for(int p : primes) {
      if(p > n) break;
      else if(n % p == 0) r = r * (p-1) / p;
    }
    return r;
  }
}
