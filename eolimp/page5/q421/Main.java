package page5.q421;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    double l = in.nextDouble(), k = in.nextInt();
    int cnt = 0;

    l /= k;
    while(l > 1.000001) {
      cnt++;
      l /= k;
    }
    System.out.println(cnt);
  }
}
