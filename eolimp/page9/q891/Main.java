package page9.q891;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {
    Scanner in = new Scanner(System.in);
    int a = in.nextInt(), b = in.nextInt(),
        c = in.nextInt(), x = c/a, y = c/b,
        m = 0, v = 0;

    for(int i=0; i<=x; i++) {
      for(int j=0; j<=y; j++) {
        int n =  i*a + j*b,
            ni = i + j;
        if(n <= c && (n > v || (n == v || ni > m))) {
          v = n;
          m = ni;
        }
      }
    }

    System.out.println(v);
  }
}
