package page3.q255;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String s = new Scanner(System.in).nextLine();
    System.out.println(getDigitalRoot(s));
  }

  private static int getDigitalRoot(String s) {
    int n = getDigitSum(s);
    return (n < 10) ? n : getDigitalRoot(String.valueOf(n));
  }

  private static int getDigitSum(String s) {
    int sum = 0;
    for(char c : s.toCharArray()) sum += c - '0';
    return sum;
  }
}
