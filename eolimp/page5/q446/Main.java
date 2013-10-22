package page5.q446;

import java.util.Scanner;

public class Main {

  public static void main(String[] args) {

    int n=new Scanner(System.in).nextInt();
    int q, d, i, cnt=0;

    for(i=1; i<=n; i++) {
      q = n / i;
      d = n - i * q;
      if(q == d) cnt++;
    }

    System.out.println(cnt);
  }

}