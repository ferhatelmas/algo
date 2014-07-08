package page13.q1214;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    long n = in.nextLong(), k = in.nextLong(), mul = n,
         limit = 1000000000000000000l;

    while(n > k) {
      n -= k;
      if(limit / mul < n) {
        System.out.println("overflow");
        return;
      }
      mul *= n;
    }
    System.out.println(mul);
  }
}
