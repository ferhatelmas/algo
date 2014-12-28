package page36.q3570;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    in.nextLine();
    while(t-- > 0) {
      String s = in.nextLine();
      System.out.println(s + " is " + isGood(s));
    }
  }

  private static String isGood(String s) {
    int g = 0, b = 0;
    for(char c : s.toLowerCase().toCharArray())
      if(c == 'g') g++;
      else if(c == 'b') b++;
    return g > b ? "GOOD" : (g == b ? "NEUTRAL" : "A BADDY");
  }
}
