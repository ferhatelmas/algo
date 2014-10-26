package page28.q2796;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine();

    BigInteger b = BigInteger.ZERO;
    for(int i=s.length()-1; i>-1; i--) {
      BigInteger n = new BigInteger(s.substring(0, i) + s.substring(i+1));
      int c = b.compareTo(n);
      if(c < 0) b = n;
    }
    System.out.println(b.toString());
  }
}
