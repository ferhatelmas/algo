package page6.q519;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    System.out.println(new BigInteger(in.next())
        .pow(2).add(new BigInteger(in.next()).pow(2)));
  }
}
