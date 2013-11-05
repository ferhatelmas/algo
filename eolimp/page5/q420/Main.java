package page5.q420;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int x = in.nextInt(), y = in.nextInt();

    double e = 81 / (Math.pow(x, 2) + Math.pow(y, 2)),
           m = 1 / (Math.pow(384000 - x, 2) + Math.pow(y, 2));

    System.out.println(e-m > 0 ? "Earth" : (m-e > 0 ? "Moon" : "Equal"));
  }
}
