package page38.q3743;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long a, b;

    while((a = in.nextInt()) != 0 && (b = in.nextInt()) != 0)
      System.out.println(2*a - b);
  }
}
