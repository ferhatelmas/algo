package page20.q1915;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();
    System.out.println((n == 1 ? BigInteger.ZERO : BigInteger.TEN.pow(n-1))
        .subtract(BigInteger.TEN.pow(in.nextInt())).abs().toString());
  }
}
