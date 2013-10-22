package page4.q388;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int n = new Scanner(System.in).nextInt(), cnt = 0;

    while(n > 1) {
      if(n%2 == 0) {
        n /= 2;
        cnt++;
      } else {
        n++;
        cnt++;
      }
    }
    System.out.println(cnt);
  }

}