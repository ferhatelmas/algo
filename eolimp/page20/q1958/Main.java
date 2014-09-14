package page20.q1958;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    in.nextLine();
    String s = in.nextLine().replaceAll("\\s", "");
    int m = in.nextInt();
    System.out.println(new BigInteger(s)
        .mod(BigInteger.valueOf(m)).intValue() == 0 ? "YES" : "NO");
  }
}
