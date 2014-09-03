package page54.q5335;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    BigInteger b = new BigInteger(in.nextLine());
    System.out.println(b.multiply(new BigInteger(in.nextLine())).toString());
  }
}
