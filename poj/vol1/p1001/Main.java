package vol1.p1001;

import java.math.BigDecimal;
import java.math.BigInteger;
import java.math.MathContext;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    while(in.hasNextDouble()) {
      String[] parts = new BigDecimal(in.nextDouble(), MathContext.DECIMAL32)
          .pow(in.nextInt()).toPlainString().split("\\.");

      if(!parts[0].startsWith("0")) System.out.print(parts[0]);

      if(parts.length > 1) {
        BigInteger dec = new BigInteger(new StringBuilder(parts[1]).reverse().toString());
        if(dec.compareTo(BigInteger.ZERO) != 0)
          System.out.println("." + new StringBuilder(dec.toString()).reverse().toString());
        else
          System.out.println();
      } else {
        System.out.println();
      }
    }
  }

}
