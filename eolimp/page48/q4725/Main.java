package page48.q4725;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    BigInteger b = new BigInteger(new Scanner(System.in).next());
    System.out.println(b
        .multiply(b.add(BigInteger.ONE))
        .multiply(b.multiply(BigInteger.valueOf(2)).add(BigInteger.ONE))
        .divide(BigInteger.valueOf(6))
        .toString());
  }
}
