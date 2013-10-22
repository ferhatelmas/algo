package page12.q1148;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);
    int t = in.nextInt();

    while(t-- > 0) {
      int g = in.nextInt(), l = in.nextInt();
      System.out.println(l%g == 0 ? (g + " " + l) : -1);
    }

  }

}
