package page3.q270;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int m = 34943;
    BigInteger b = new BigInteger(new Scanner(System.in).nextLine().getBytes()),
               d = BigInteger.valueOf(m);

    b = b.shiftLeft(16);
    String s = Integer.toHexString(m - b.mod(d).intValue()).toUpperCase();
    for(int i=4-s.length(); i>0; i--)
      s = "0" + s;
    System.out.println(s.substring(0, 2) + " " + s.substring(2));
  }
}
