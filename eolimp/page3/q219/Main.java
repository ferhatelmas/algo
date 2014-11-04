package page3.q219;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double v = in.nextLong() * in.nextInt() * in.nextInt(),
           t = in.nextInt();
    System.out.println((int)Math.ceil(v/t));
  }
}
