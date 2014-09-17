package page23.q2292;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    BigInteger fibs[] = new BigInteger[10001];
    fibs[0] = BigInteger.ZERO;
    fibs[1] = BigInteger.ONE;
    for(int i=2; i<fibs.length; i++)
      fibs[i] = fibs[i-1].add(fibs[i-2]);

    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    while(n-- > 0)
      System.out.println(fibs[in.nextInt()].toString());
  }
}
