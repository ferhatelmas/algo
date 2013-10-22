package page24.q2385;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), p = 1;
    for(int i=2; i<=n; i++) p *= i;
    System.out.println(p);
  }
}
