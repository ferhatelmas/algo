package page51.q5093;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    System.out.println(new BigInteger(new Scanner(System.in).nextLine())
        .mod(BigInteger.valueOf(13)).intValue());
  }
}
