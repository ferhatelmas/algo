package page3.q252;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(new BigInteger(in.next())
        .modPow(new BigInteger(in.next()), new BigInteger(in.next())));
  }
}
