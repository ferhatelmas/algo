package page42.q4102;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      String a = in.next().toLowerCase(), b = in.next().toLowerCase();
      System.out.println(b + "." + a + "@retratek.com");
    }
  }
}
