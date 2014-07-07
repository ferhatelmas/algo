package page29.q2804;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    double c = 0;
    for(char ch : new Scanner(System.in).nextLine().toCharArray())
      c += ch - '0';
    c = Math.sqrt(c);
    System.out.println((c - (int)c < 0.000001) ? "Yes" : "No");
  }
}
