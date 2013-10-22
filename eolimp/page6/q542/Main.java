package page6.q542;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int e = in.nextInt() + in.nextInt(), c = in.nextInt(), cnt = 0;
    while(e >= c) {
      int n = e/c;
      cnt += n;
      e = n + e%c;
    }
    System.out.println(cnt);
  }
}
