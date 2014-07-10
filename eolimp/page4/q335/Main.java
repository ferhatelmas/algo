package page4.q335;

import java.util.Scanner;

public class Main {
  public static void main(String[] argv) {
    Scanner in = new Scanner(System.in);

    int t = in.nextInt();
    while(t-- > 0) {
      int n = in.nextInt(), i = 0;
      boolean r = false;

      while(i++ < n) {
        if(n%i == 0) r = !r;
      }
      System.out.println(r ? "1" : "0");
    }
  }
}
