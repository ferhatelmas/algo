package page74.q7336;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(), n = in.nextInt();
    a *= n;
    System.out.println((a + (b*n/100)) + " " + (b*n)%100);
  }
}
