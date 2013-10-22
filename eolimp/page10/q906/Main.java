package page10.q906;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int r = new Scanner(System.in).nextInt();

    int d1 = r/100;
    int d2 = r%100/10;
    int d3 = r%10;

    System.out.println(d1*d2*d3);
  }

}