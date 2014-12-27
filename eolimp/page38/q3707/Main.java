package page38.q3707;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int p = in.nextInt(), n = in.nextInt();
    BigInteger a = BigInteger.valueOf(p),
               b = BigInteger.TEN.pow(16),
               c = a;

    for(int i=1; i<n; i++)
      a = c.modPow(a, b);
    System.out.println(a.toString());
  }
}
