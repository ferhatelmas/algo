package page51.q5086;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int c = new BigInteger(in.next()).compareTo(new BigInteger(in.next()));
    System.out.println(c == 0 ? "=" : (c < 0 ? "<" : ">"));
  }
}
