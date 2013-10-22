package page10.q903;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int r = new Scanner(System.in).nextInt();

    int d1 = r/100;
    int d2 = r%100/10;
    int d3 = r%10;

    if(d1 < d2) {
      if(d2 < d3) System.out.println(d3);
      else if(d2 == d3) System.out.println("=");
      else System.out.println(d2);
    } else {
      if(d1 < d3) System.out.println(d3);
      else if(d1 == d3) System.out.println("=");
      else System.out.println(d1);
    }

  }

}