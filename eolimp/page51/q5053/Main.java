package page51.q5053;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    String d = in.next();
    System.out.println(new BigInteger(in.next()).mod(new BigInteger(d)).toString());
  }
}
