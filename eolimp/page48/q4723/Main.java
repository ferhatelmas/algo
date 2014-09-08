package page48.q4723;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), c = 0;

    while(n-- > 0)
      if(in.nextInt() == 0) c++;
    System.out.println(c);
  }
}
