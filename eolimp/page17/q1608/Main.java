package page17.q1608;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).next();
    System.out.println(isPalindrome(s) ? "Yes" : "No");
  }

  private static boolean isPalindrome(String s) {
    return s.equals(new StringBuilder(s).reverse().toString());
  }
}
