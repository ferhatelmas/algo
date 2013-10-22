package page10.q905;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    Scanner in = new Scanner(System.in);

    int x, y, z;
    x = in.nextInt();
    y = in.nextInt();
    z = in.nextInt();

    if(x==y && y==z) System.out.println("1");
    else if(x==y || x==z || y == z) System.out.println("2");
    else System.out.println("3");
  }

}