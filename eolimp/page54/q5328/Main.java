package page54.q5328;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt()-1, m = in.nextInt();
    while(n-- > 0)
      m = Math.min(m, in.nextInt());
    System.out.println(m);
  }
}
