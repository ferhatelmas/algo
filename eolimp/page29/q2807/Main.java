package page29.q2807;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), c = 0;
    for(char ch : in.next().toCharArray())
      c ^= ch;
    System.out.println(c == 0 ? "Ok" : (char)c);
  }
}
