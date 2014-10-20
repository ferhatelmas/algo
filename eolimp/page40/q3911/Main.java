package page40.q3911;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    BigInteger res[] = new BigInteger(in.next()).divideAndRemainder(new BigInteger(in.next()));
    System.out.println(res[0].toString() + " " + res[1].toString());
  }
}
