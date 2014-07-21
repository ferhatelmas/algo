package page6.q577;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), s = 4;

    while(n > 0) {
      n -= getDigitCount(s++);
    }
    System.out.println(s-1);
  }

  private static int getDigitCount(int n) {
    return String.valueOf(n).length();
  }
}
