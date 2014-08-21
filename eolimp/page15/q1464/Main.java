package page15.q1464;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n;

    while((n = in.nextInt()) != 0) {
      if(n < 0)
        System.out.println(-(n * (n-1) / 2) + 1);
      else
        System.out.println((n * (n + 1)) / 2);
    }
  }
}
