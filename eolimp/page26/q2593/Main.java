package page26.q2593;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long n = in.nextLong();
    String m = in.next();
    for(int i=getMaxDigit(m)+1; i<10; i++)
      try {
        if(n == Long.parseLong(m, i)) {
          System.out.println(i);
          break;
        }
      } catch (NumberFormatException e) {}
  }

  private static int getMaxDigit(String s) {
    int max = 0;
    for(char c : s.toCharArray())
      max = Math.max(max, c-'0');
    return max;
  }
}
