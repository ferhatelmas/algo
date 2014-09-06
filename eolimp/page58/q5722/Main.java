package page58.q5722;

import java.math.BigInteger;
import java.util.Scanner;

// Not enough memory for Java
public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), i = 0, c = 0;

    while(i++ < n)
      if(new BigInteger(in.next()).bitCount() == 1) c++;
    System.out.println(c);
  }
}
