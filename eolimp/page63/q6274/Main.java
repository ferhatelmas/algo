package page63.q6274;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    System.out.println((int)(Math.sqrt(1 + 8 * (in.nextInt() - in.nextInt())) - 1) / 2);
  }
}
