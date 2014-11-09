package page2.q165;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();

    if(isPowerOfTwo(n))
      System.out.println(getPower(n));
    else {
      int k = 1;
      while((n-k) % (k*2) != 0)
        k *= 2;
      System.out.println(getPower(k));
    }
  }

  private static int getPower(int n) {
    return (int)(Math.log(n) / Math.log(2)) + 1;
  }

  private static boolean isPowerOfTwo(int n) {
    return ((n != 0) && (n & (n - 1)) == 0);
  }
}
