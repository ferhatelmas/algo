package page29.q2806;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println(n - n/2 - n/3 - n/5 - n/30 + n/6 + n/10 + n/15);
  }
}
