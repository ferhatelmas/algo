package page21.q2014;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    String[] s = new Scanner(System.in).next().split("\\.");
    System.out.println(sum(s[0]) == sum(s[1]) ? "Yes" : "No");
  }

  private static int sum(String s) {
    if(s.startsWith("-")) s = s.substring(1);
    int sum = 0;
    for(char c : s.toCharArray())
      sum += c - '0';
    return sum;
  }
}
