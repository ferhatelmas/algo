package page27.q2695;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    BigInteger bb = new BigInteger(new Scanner(System.in).next(), 2);
    int a = bb.mod(new BigInteger("3")).intValue(),
        b = bb.mod(new BigInteger("5")).intValue();
    if((a|b) == 0) System.out.println("BOTH");
    else if(a == 0) System.out.println("FIRST");
    else if(b == 0) System.out.println("SECOND");
    else System.out.println("NONE");
  }
}
