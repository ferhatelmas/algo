package page2.q192;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), cnt = 0, a = 1, b = 1, t;

    while(cnt < n) {
      t = a + b;
      b = a;
      a = t;
      if(isPrime(a)) cnt++;
    }
    System.out.println(a);
  }

  private static boolean isPrime(int n) {
    for(int i=2; i<=Math.sqrt(n); i++) if(n%i == 0) return false;
    return true;
  }
}
