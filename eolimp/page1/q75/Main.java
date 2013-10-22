package page1.q75;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner sc = new Scanner(System.in);

    int a = sc.nextInt();
    int m = sc.nextInt();

    int delta = (2*a+1) * (2*a+1) - 4 * (-2*m+2*a-2);
    int x1 = (-(2*a+1) - (int)Math.sqrt(delta)) / 2;
    int x2 = (-(2*a+1) + (int)Math.sqrt(delta)) / 2;

    System.out.println(Math.max(x1, x2));
  }

}