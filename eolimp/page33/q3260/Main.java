package page33.q3260;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int n = in.nextInt(), k = in.nextInt(), mul = 1;

    for(int i=n; i>n-k; i--)
      mul *= i;
    for(int i=2; i<=k; i++)
      mul /= i;
    System.out.println(mul);
  }
}
