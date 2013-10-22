package page16.q1514;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    long k = in.nextLong(), n = in.nextLong();
    int t = in.nextInt(), i = 0;

    while(!(k == 0 && n == 0 && t == 0)) {
      System.out.println("Case #" + ++i + ": " + x(k, n, t));
      k = in.nextLong(); n = in.nextLong();
      t = in.nextInt();
    }
  }

  private static String x(long k, long n, int t) {
    return new BigInteger(String.valueOf(k))
        .modPow(new BigInteger(String.valueOf(n)), new BigInteger(String.valueOf((int)Math.pow(10, t))))
        .toString();
  }
}
