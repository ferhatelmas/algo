package page48.q4719;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(),
        b = in.nextInt(),
        c = in.nextInt(),
        d = in.nextInt();

    if((a == c && b != d) || (a != c && b == d))
      System.out.println("YES");
    else
      System.out.println("NO");
  }
}
