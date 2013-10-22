package page24.q2396;

import java.util.Scanner;

public class Main {

  private static final String[] u19 = {"one", "two", "three", "four", "five", "six", "seven",
      "eight", "nine", "ten", "eleven", "twelve", "thirteen",
      "fourteen", "fifteen", "sixteen", "seventeen", "eighteen", "nineteen"},
      u10s = {"ten", "twenty", "thirty", "forty", "fifty", "sixty", "seventy", "eighty", "ninety"};
  private static final String u100 = "hundred";

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();

    StringBuilder sb = new StringBuilder();
    while(n > 0) {
      if(n > 99) {
        sb.append(u19[n/100-1]).append(" ").append(u100).append(" ");
        n %= 100;
      } else if(n > 19) {
        sb.append(u10s[n/10-1]).append(" ");
        n %= 10;
      } else {
        sb.append(u19[n-1]).append(" ");
        n = 0;
      }
    }
    System.out.println(sb.toString().trim());
  }
}
