package page10.q961;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    System.out.println((n/1000) * 10 + n%10);
  }
}
