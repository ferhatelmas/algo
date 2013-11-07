package page6.q511;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int n = in.nextInt(), k = in.nextInt(), a = 1, b = n, cnt = 1, m = (a + b) / 2;

    while(m != k) {
      if(m > k) b = m - 1;
      else  a = m + 1;
      m = (a + b) / 2;
      cnt++;
    }
    System.out.println(cnt);
  }
}
