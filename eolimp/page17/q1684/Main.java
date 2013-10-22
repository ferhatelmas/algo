package page17.q1684;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), c = 64, cost = 1;

    while(n > 0) {
      n -= 60;
      cost += c;
      c = Math.max(1, c/2);
    }
    System.out.println(cost);
  }
}
