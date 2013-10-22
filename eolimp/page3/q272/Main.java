package page3.q272;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println(new BigInteger(in.nextLine())
        .multiply(new BigInteger(in.nextLine())));
  }
}
