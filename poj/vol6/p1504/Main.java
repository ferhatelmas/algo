package vol6.p1504;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      int i = Integer.parseInt(new StringBuilder(in.next()).reverse().toString());
      int j = Integer.parseInt(new StringBuilder(in.next()).reverse().toString());

      System.out.println(Integer.parseInt(new StringBuilder(String.valueOf(i+j)).reverse().toString()));
    }
  }
}
