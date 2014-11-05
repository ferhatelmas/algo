package page2.q126;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), p = in.nextInt(),
        q = in.nextInt(), k = in.nextInt(),
        c = n/p, d = c/q;

    int e = (int)Math.ceil((double)k / c),
        f = (int)Math.ceil((double)(k - (e-1) * c) / d);
    System.out.println(e + " " + f);
  }
}
