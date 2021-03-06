package page4.q366;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    BigInteger n = new BigInteger(new Scanner(System.in).next());

    for(int i=1; i<1001; i++) {
      for(int j=1; j<10; j++) {
        StringBuilder sb = new StringBuilder();
        for(int k=0; k<i; k++) {
          sb.append(j);
        }
        BigInteger sum = new BigInteger(sb.toString());
        if(sum.mod(n).compareTo(BigInteger.ZERO) == 0) {
          System.out.println(j + " " + i);
          return;
        }
      }
    }
    System.out.println("0 0");
  }
}
