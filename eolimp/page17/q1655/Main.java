package page17.q1655;

import java.math.BigInteger;
import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    boolean[] sieve = new boolean[1001];
    Arrays.fill(sieve, true);

    for(int i=2; i<sieve.length; i++)
      if(sieve[i])
        for(int j=2*i; j<sieve.length; j+=i)
          sieve[j] = false;
    int n = new Scanner(System.in).nextInt();
    BigInteger lcm = BigInteger.ONE;
    for(int i=2; i<=n; i++)
      if(sieve[i])
        lcm = lcm.multiply(getMul(n, i));

    System.out.println(lcm);
  }

  private static BigInteger getMul(int n, int i) {
    int cnt = 0;
    while(n >= i) {
      cnt++;
      n /= i;
    }
    return new BigInteger(String.valueOf((int)Math.pow(i, cnt)));
  }

}
