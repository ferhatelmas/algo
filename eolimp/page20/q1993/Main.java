package page20.q1993;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt();
    if(n < 4) n = 1;
    else if(n < 10) n = 2;
    else n = 3;
    System.out.println(n);
  }
}
