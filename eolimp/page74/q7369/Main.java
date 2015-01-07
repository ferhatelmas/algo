package page74.q7369;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt();
    a += (10-a%7)%7;
    b -= (3-b%7)%7;
    System.out.println((b-a)/7 + (b>=a ? 1 : 0));
  }
}
