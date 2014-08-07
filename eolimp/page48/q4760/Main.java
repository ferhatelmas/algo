package page48.q4760;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = (int)Math.pow(in.nextInt(), 2), cnt = 0;

    while(n-- > 0) {
      cnt += in.nextInt();
    }
    System.out.println(cnt / 2);
  }
}
