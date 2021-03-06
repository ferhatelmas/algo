package page39.q3843;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    boolean sieve[] = new boolean[10000001];
    Arrays.fill(sieve, true);
    sieve[0] = sieve[1] = false;

    for(int i=2; i<sieve.length; i++)
      if(sieve[i])
        for(int j=2*i; j<sieve.length; j+=i)
          sieve[j] = false;

    boolean f = false;
    while(in.hasNextInt()) {
      int c = 0;
      for(int i=in.nextInt(), j=in.nextInt(); i<=j; i++)
        if(sieve[i]) c++;
      if(!f) f = !f;
      else System.out.println();
      System.out.println(c);
    }
  }
}
