package page38.q3742;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    BigInteger b = new BigInteger(in.next());
    System.out.println(b.modPow(b, BigInteger.TEN.pow(in.nextInt())).toString());
  }
}
