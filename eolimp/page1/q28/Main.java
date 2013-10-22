package page1.q28;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) throws Exception {
    BigInteger r = new BigInteger(new Scanner(System.in).nextLine()), curr;

    for(int i=2; i<=10000; i++) {
      curr = BigInteger.ONE;
      for(int j=i; j<=10000; j++) {
        curr = curr.multiply(new BigInteger(String.valueOf(j)));
        int cmp = curr.compareTo(r);
        if(cmp == 0) {
          System.out.println(i + " " + j);
          return;
        } else if(cmp > 0)
          break;
      }
    }
  }
}
