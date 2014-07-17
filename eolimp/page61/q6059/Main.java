package page61.q6059;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);

    int t = in.nextInt();
    while(t-- > 0) {
      int n = in.nextInt();
      System.out.println((int)Math.pow((n+1)/2, 2));
    }
  }
}
