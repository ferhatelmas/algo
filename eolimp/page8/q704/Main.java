package page8.q704;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    StringBuilder sb = new StringBuilder();
    while(t-- > 0) {
      sb.append(getLeastSignificant(in.nextInt())).append('\n');
    }
    System.out.print(sb.toString());
  }

  private static char getLeastSignificant(int n) {
    char c = '0';
    for(char ch : fact(n))
      if(ch != '0') c = ch;
    return c;
  }

  private static char[] fact(int n) {
    BigInteger b = BigInteger.ONE;
    for(int i=2; i<=n; i++)
      b = b.multiply(new BigInteger(String.valueOf(i)));
    return b.toString().toCharArray();
  }
}
