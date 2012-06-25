package com.ferhatelmas.euler.page2;

import java.math.BigInteger;
import java.util.Arrays;

public class Question66 {

  public static void main(String[] args) {

    boolean[] primes = new boolean[1001];
    Arrays.fill(primes, true);

    long max = 2; BigInteger maxValue = BigInteger.ZERO;
    for(int i=2; i<primes.length; i++) {
      if(primes[i]){

        BigInteger tmp = pell(i);
        if(tmp.compareTo(maxValue) == 1) {
          max = i;
          maxValue = tmp;
        }

        for(int j=2*i; j<primes.length; j+=i) {
          primes[j] = false;
        }

      }
    }

    System.out.println(max);
  }

  private static BigInteger pell(int d) {

    int m = 1, k = 1;
    BigInteger x = new BigInteger("1"), y = new BigInteger("0");
    double sd = Math.sqrt(d);

    while(k != 1 || y.equals(BigInteger.ZERO)) {
      m = k * (m/k + 1) - m;
      m = m - (int)((m - sd)/k) * k;

      BigInteger xt = x.multiply(BigInteger.valueOf(m))
          .add(y.multiply(BigInteger.valueOf(d)))
          .divide(BigInteger.valueOf(Math.abs(k)));
      y = x.add(y.multiply(BigInteger.valueOf(m))
          .divide(BigInteger.valueOf(Math.abs(k))));

      x = xt;
      k = (m*m - d) / k;
    }

    return x;
  }
}
