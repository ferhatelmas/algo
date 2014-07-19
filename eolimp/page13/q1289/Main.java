package page13.q1289;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long a = in.nextLong(), b = in.nextLong(), c = in.nextLong();
    System.out.println(a*b + a*c + b*c);
  }
}
