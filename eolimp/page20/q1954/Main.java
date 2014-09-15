package page20.q1954;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(n - (int)Math.pow((int)Math.sqrt(n), 2));
  }
}
