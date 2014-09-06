package page51.q5083;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), mv = Integer.MAX_VALUE, m = 0;

    while(n-- > 0) {
      int t = in.nextInt(), tv = getDigitSum(t);
      if(tv <= mv) {
        m = t;
        mv = tv;
      }
    }
    System.out.println(m);
  }

  private static int getDigitSum(int n) {
    int sum = 0;
    for(char c : String.valueOf(Math.abs(n)).toCharArray())
      sum += c - '0';
    return sum;
  }
}
