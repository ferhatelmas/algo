package page74.q7338;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), c = 0;
    for(int i=10; i<100; i++)
      if(getDigitSum(i) == getDigitSum(i * n)) c++;
    System.out.println(c);
  }

  private static int getDigitSum(int n) {
    int sum = 0;
    for(char c : String.valueOf(n).toCharArray())
      sum += c - '0';
    return sum;
  }
}
