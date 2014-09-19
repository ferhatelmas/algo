package page18.q1780;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long n;
    while(in.hasNextLong()) {
      n = in.nextLong();
      System.out.println((n >> 1) ^ n);
    }
  }
}
