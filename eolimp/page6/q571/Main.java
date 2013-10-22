package page6.q571;

import java.util.Arrays;
import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int n = in.nextInt();
    int[] numbers = new int[n];
    for(int i=0; i<n; i++) numbers[i] = in.nextInt();
    Arrays.sort(numbers);

    n = numbers[0];
    for(int i=1; i<numbers.length; i++)
      n = gcd(n, numbers[i]);

    System.out.println(n);
  }

  private static int gcd(int a, int b) {
    int t;
    while(b != 0) {
      t = a;
      a = b;
      b = t%b;
    }
    return a;
  }

  private static int gcd2(int a, int b) {
    return b == 0 ? a : gcd2(b, a%b);
  }

}
