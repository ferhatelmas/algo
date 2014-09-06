package page51.q5051;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt();
    System.out.println((((a << 5) + (a << 2) + (b >> 4)) & (0x1f)));
  }
}
