package page48.q4757;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    BigInteger b = new BigInteger(new Scanner(System.in).next(), 2);
    System.out.println(b.mod(new BigInteger("15")).intValue() == 0 ? "YES" : "NO");
  }
}
