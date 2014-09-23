package page62.q6190;

import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    boolean sieve[] = new boolean[1000001];
    Arrays.fill(sieve, true);
    for(int i=2; i<sieve.length; i++)
      if(sieve[i])
        for(int j=2*i; j<sieve.length; j+=i)
          sieve[j] = false;
    long n = new Scanner(System.in).nextLong();
    for(int i=2; i<sieve.length; i++) {
      if(sieve[i]) {
        int j = i+1;
        while(j < sieve.length && !sieve[j]) j++;
        if(j < sieve.length && i * (long)j == n) {
          System.out.println(i + " " + j);
          return;
        }
      }
    }
  }
}
