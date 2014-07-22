package page7.q637;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(new BigInteger("2").pow(n * n)
                                          .subtract(BigInteger.ONE)
                                          .toString());
  }
}
