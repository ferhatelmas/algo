package page73.q7292;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long total = getMoney(in.nextInt(), in.nextInt(), in.nextInt()),
        t = in.nextInt(), sum = 0;

    while(t-- > 0) {
      sum += getMoney(in.nextInt(), in.nextInt(), in.nextInt());
    }
    long k = Math.max(total - sum, -1);
    if(k < 0) System.out.println(k);
    else System.out.println(c(k));
  }

  private static String c(long n) {
    long a = n / (17 * 29),
         b = (n % (17 * 29)) / 29,
         c = n % 29;
    return a + " " + b + " " + c;
  }

  private static long getMoney(long a, long b, long c) {
    return 17 * 29 * a + 29 * b + c;
  }
}
