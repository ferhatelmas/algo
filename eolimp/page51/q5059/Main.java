package page51.q5059;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = Integer.MAX_VALUE, b = Integer.MAX_VALUE, n = in.nextInt(), c;
    while(n-- > 0) {
      c = in.nextInt();
      if(c < a) {
        b = a;
        a = c;
      } else if(c < b) {
        b = c;
      }
    }
    System.out.println(a + " " + b);
  }
}
