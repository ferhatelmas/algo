package page48.q4747;

import java.util.Scanner;

public class Main {
  public static void main(String[] args) {
    int n = new Scanner(System.in).nextInt(), cnt, i = 2;

    while(n > 1) {
      cnt = 0;
      while(n%i == 0) {
        n /= i;
        cnt++;
      }
      if(cnt > 0)
        System.out.println(i + " " + cnt);
      i++;
    }
  }
}
