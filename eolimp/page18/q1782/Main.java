package page18.q1782;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    long n = new Scanner(System.in).nextLong();
    boolean primes[] = new boolean[1001];
    Arrays.fill(primes, true);

    BigInteger b = BigInteger.ONE;
    for(int i=2; i<primes.length; i++)
      if(primes[i]) {
        int cnt = 0;
        while(n % i == 0) {
          n /= i;
          cnt++;
        }
        if(cnt > 0) {
          b = b.multiply(new BigInteger(String.valueOf((long)(Math.pow(i, cnt+1)-1) / (i-1))));
          if(n == 1) break;
        }
        for(int j=2*i; j<primes.length; j+=i)
          primes[j] = false;
      }
    System.out.println(b.toString());
  }
}
