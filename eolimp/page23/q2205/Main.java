package page23.q2205;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int m = in.nextInt(), n = in.nextInt(), k = in.nextInt(),
        c = ((n-1) / k) * k + 1, min = (n - c) * 200;

    if(c + k <= m) min = Math.min(min, (c + k - n) * 100);
    System.out.println(min);
  }
}
