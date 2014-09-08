package page48.q4722;

import java.math.BigInteger;
import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt();
    StringBuilder sb = new StringBuilder();
    while(k-- > 0) sb.append(n);
    System.out.println(new BigInteger(sb.toString()).pow(2).toString());
  }
}
