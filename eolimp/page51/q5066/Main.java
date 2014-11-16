package page51.q5066;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    BigInteger b = new BigInteger(in.nextLine()),
        c = new BigInteger(in.nextLine());
    BigInteger r[] = b.divideAndRemainder(c);
    System.out.println(r[0].toString());
    System.out.println(r[1].toString());
  }
}

