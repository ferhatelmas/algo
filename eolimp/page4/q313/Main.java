package page4.q313;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt();

    in.nextLine();
    while(n-- > 0) {
      String s = in.nextLine();
      int k = s.indexOf('+');
      System.out.println(new BigInteger(s.substring(0, k)).add(new BigInteger(s.substring(k+1))));
    }
  }
}
