package page3.q271;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), cnt = 1;
    BigInteger res = BigInteger.ONE;

    while(cnt <= n)
      res = res.multiply(new BigInteger(String.valueOf(cnt++)));
    System.out.println(res);
  }
}
