package page29.q2801;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n2 = in.nextInt(), k = in.nextInt();
    System.out.println(k*k <= n2 ? 2*k-1 : -1);
  }
}
